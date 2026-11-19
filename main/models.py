from django.db import models

MAX_LENGTH = 255

PROJECT_STATUSES = [
    ('planned', 'Планируется'),
    ('active', 'В работе'),
    ('paused', 'Приостановлен'),
    ('done', 'Завершён'),
]

CONTRACT_STATUSES = [
    ('draft', 'Проект'),
    ('active', 'Действует'),
    ('done', 'Исполнен'),
    ('terminated', 'Расторгнут'),
]


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование отдела')
    created_date = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Position(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование должности')
    hourly_rate = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Часовая ставка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    GENDERS = [('М', 'Мужской'), ('Ж', 'Женский')]

    full_name = models.CharField(max_length=300, verbose_name='ФИО')
    gender = models.CharField(max_length=1, choices=GENDERS, verbose_name='Пол')
    passport = models.CharField(max_length=20, verbose_name='Паспорт')
    birth_date = models.DateField(verbose_name='Дата рождения')
    hire_date = models.DateField(verbose_name='Дата приёма')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Email')
    characteristic = models.TextField(null=True, blank=True, verbose_name='Характеристика')
    photo = models.ImageField(upload_to='employees/%Y/%m/%d', null=True, blank=True, verbose_name='Фото')

    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='Отдел')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название организации')
    contact_person = models.CharField(max_length=300, verbose_name='Контактное лицо')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Email')
    address = models.TextField(verbose_name='Адрес')
    inn = models.CharField(max_length=20, unique=True, verbose_name='ИНН')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование проекта')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='projects/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    start_date = models.DateField(verbose_name='Дата начала')
    end_plan_date = models.DateField(verbose_name='Плановая дата окончания')
    end_fact_date = models.DateField(null=True, blank=True, verbose_name='Фактическая дата окончания')
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Стоимость проекта')
    status = models.CharField(max_length=50, choices=PROJECT_STATUSES, default='planned', verbose_name='Статус')

    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Руководитель проекта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Contract(models.Model):
    number = models.CharField(max_length=100, verbose_name='Номер договора')
    sign_date = models.DateField(verbose_name='Дата заключения')
    expire_date = models.DateField(verbose_name='Дата истечения')
    total_cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Суммарная стоимость')
    payment_method = models.CharField(max_length=50, verbose_name='Метод оплаты')
    status = models.CharField(max_length=50, choices=CONTRACT_STATUSES, default='draft', verbose_name='Статус')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='Руководитель договора')
    projects = models.ManyToManyField(Project, blank=True, related_name='contracts', verbose_name='Проекты')

    def __str__(self):
        return f'Договор № {self.number}'

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class Equipment(models.Model):
    inventory_number = models.CharField(max_length=50, unique=True, verbose_name='Инвентарный номер')
    name = models.CharField(max_length=200, verbose_name='Наименование')
    equipment_type = models.CharField(max_length=100, verbose_name='Тип оборудования')
    photo = models.ImageField(upload_to='equipment/%Y/%m/%d', null=True, blank=True, verbose_name='Фото')
    receipt_date = models.DateField(verbose_name='Дата поступления')
    initial_cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Первоначальная стоимость')
    condition = models.CharField(max_length=200, verbose_name='Состояние')

    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True,
                                   verbose_name='Отдел-владелец')

    def __str__(self):
        return f'{self.name} ({self.inventory_number})'

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'


class WorkGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование группы')
    code = models.CharField(max_length=50, verbose_name='Код группы')
    created_date = models.DateField(verbose_name='Дата создания')
    disbanded_date = models.DateField(null=True, blank=True, verbose_name='Дата расформирования')

    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='led_groups', verbose_name='Руководитель группы')
    members = models.ManyToManyField(Employee, blank=True, related_name='work_groups', verbose_name='Участники')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рабочая группа'
        verbose_name_plural = 'Рабочие группы'