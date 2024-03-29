from django.db import models

# Create your models here.

class Car(models.Model):
    BODY_CHOICES = [
        ('S', 'Sedan'),
        ('HB', 'Hatchback'),
        ('SUV', 'SUV'),
        ('CO', 'Crossover'),
        ('C', 'Coupe'),
        ('Co', 'Convertible'),
        ('W', 'Wagon'),
        ('V', 'Van'),
        ('MV', 'Minivan'),
        ('P', 'Pickup'),
        ('T', 'Truck'),
        ('B', 'Bus'),
        ('Ot', 'Other'),
    ]

    BRAND_CHOICES = [
        ('Acura', 'Acura'),
        ('Alfa Romeo', 'Alfa Romeo'),
        ('Aston Martin', 'Aston Martin'),
        ('Audi', 'Audi'),
        ('Bentley', 'Bentley'),
        ('BMW', 'BMW'),
        ('Bugatti', 'Bugatti'),
        ('Buick', 'Buick'),
        ('Cadillac', 'Cadillac'),
        ('Chevrolet', 'Chevrolet'),
        ('Chrysler', 'Chrysler'),
        ('Citroen', 'Citroen'),
        ('Dodge', 'Dodge'),
        ('Ferrari', 'Ferrari'),
        ('Fiat', 'Fiat'),
        ('Ford', 'Ford'),
        ('Geely', 'Geely'),
        ('General Motors', 'General Motors'),
        ('GMC', 'GMC'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Infiniti', 'Infiniti'),
        ('Jaguar', 'Jaguar'),
        ('Jeep', 'Jeep'),
        ('Kia', 'Kia'),
        ('Koenigsegg', 'Koenigsegg'),
        ('Lamborghini', 'Lamborghini'),
        ('Land Rover', 'Land Rover'),
        ('Lexus', 'Lexus'),
        ('Lincoln', 'Lincoln'),
        ('Lotus', 'Lotus'),
        ('Maserati', 'Maserati'),
        ('Mazda', 'Mazda'),
        ('McLaren', 'McLaren'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mini', 'Mini'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Pagani', 'Pagani'),
        ('Peugeot', 'Peugeot'),
        ('Porsche', 'Porsche'),
        ('Ram', 'Ram'),
        ('Renault', 'Renault'),
        ('Rolls Royce', 'Rolls Royce'),
        ('Saab', 'Saab'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
        ('Ot', 'Other'),
    ]

    MODEL_CHOICES = []

    LIFE_STYELE_CHOICES = [
        ('F', 'Family'),
        ('S', 'Sport'),
        ('L', 'Luxury'),
        ('C', 'Classic'),
        ('E', 'Envoirment'),
        ('Ot', 'Other'),
    ]

    YEAR_CHOICES = []

    FULE_TYPE_CHOICES = [
        ('G', 'Gasoline'),
        ('D', 'Diesel'),
        ('E', 'Electric'),
        ('H', 'Hybrid'),
        ('Ot', 'Other'),
    ]

    COLOR_CHOICES = [
        ('B', 'Black'),
        ('W', 'White'),
        ('S', 'Silver'),
        ('G', 'Gray'),
        ('R', 'Red'),
        ('B', 'Blue'),
        ('Y', 'Yellow'),
        ('O', 'Orange'),
        ('P', 'Purple'),
        ('Ot', 'Other'),
    ]

    TRANSMISSION_CHOICES = [
        ('A', 'Automatic'),
        ('M', 'Manual'),
        ('Ot', 'Other'),
    ]
    
    BODY_STATUS_CHOICES = [
        ('E', 'Excellent'),
        ('G', 'Good'),
        ('A', 'Average'),
        ('B', 'Bad'),
        ('Ot', 'Other'),
    ]

    CUSTOMS_CASE_CHOICES = [
        ('C', 'Cleared'),
        ('N', 'Not Cleared'),
        ('Ot', 'Other'),
    ]

    body_style = models.CharField(max_length=14, choices=BODY_CHOICES, null=True, blank=True)
    brand = models.CharField(max_length=53, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50, choices=MODEL_CHOICES, null=True, blank=True)
    life_style = models.CharField(max_length=7, choices=LIFE_STYELE_CHOICES, null=True, blank=True)
    year = models.CharField(max_length=50, choices=YEAR_CHOICES, null=True, blank=True)
    fule_type = models.CharField(max_length=6, choices=FULE_TYPE_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=11, choices=COLOR_CHOICES, null=True, blank=True)
    price = models.FloatField(max_length=50, null=True, blank=True)
    mileage = models.FloatField(max_length=50, null=True, blank=True)
    transmission = models.CharField(max_length=4, choices=TRANSMISSION_CHOICES, null=True, blank=True)
    body_status = models.CharField(max_length=6, choices=BODY_STATUS_CHOICES, null=True, blank=True)
    customs_case = models.CharField(max_length=4, choices=CUSTOMS_CASE_CHOICES, null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    engine_description = models.CharField(max_length=50, null=True, blank=True)
    engine_capacity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    safety_and_technology = models.CharField(max_length=50, null=True, blank=True)
    front_style_image = models.ImageField(upload_to='images/', null=True, blank=True)
    back_style_image = models.ImageField(upload_to='images/', null=True, blank=True)
    front_style_description = models.CharField(max_length=50, null=True, blank=True)
    back_style_description = models.CharField(max_length=50, null=True, blank=True)
    strengh_points = models.CharField(max_length=50, null=True, blank=True)
    weaknesses = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.brand