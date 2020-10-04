import os, django, random, decimal

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maskes.settings")
django.setup()

from faker import Faker
from django.contrib.auth import get_user_model
from requests.models import Request
from django.utils import timezone
from requests.request_form_choices import *

GROCERY_LIST = ["Whole milk, fruit (strawberries and bananas), fruit roll ups, Minute Maid jug , orange juice , jumbolia mix, muffins, bread, noodles, Mac & cheese, caprisuns, juice boxes, pull ups 3T-4T",
"2 containers whole milk, 1 loaf white bread, 2 dozzen eggs, snacks for 8 year old (must be peanut free, fruit snacks, crackers, boxed juice, etc).",
"I bag of white rice, 4 chicken breasts, 2 onion, garlic, spinach, Clorox cleaning spray or disentfectant spray, fruit (banana and strawberry), 1 bottle shampoo and 1 bottle conditioner",
"Pañales.toallas para limpiar bb.aceite.jabon de lavar ropa.jabon de lavar trastes .frutas y verduras ",
"Jabón de lavar ropa.pañales .tuallas para limpiar bb.frutas y verduras .aceite..pañales .jabón de lavar trastes (copied from previous duplicate request: Pañales.toallas para limpiar bb.aceite.jabon de lavar ropa.jabon de lavar trastes .frutas y verduras )",
"Box of Honest diapers size 3 one size 4 , baby wipes , Red Gatorade , Lysol cleaner , bleach Clorox , glade candle , Hot Cheetos, strawberries, Minute Maid jug , fruit roll ups , Nivia coco butter lotion ",
"Pollo (whole chicken), bisteks (beef flanks steaks if at a good price), frozen shrimp in the bag,chiles verdes (sererano and jalapeno), onions, tomatos, lettuce, potatoes, carrot, queso (de rancho or cotija), cereal (something for kids like honey nut cheerios), whole milk, eggs, orange or apple juice, corn tortillas, dried beans (pinto, but black is ok), rice, cooking oil - mazola, mangoes, banana, manzana, (if cherries or strawberries are affordable- the kids love them), toilet paper, dish soap, laundry soap, toothpaste, shampoo & condicioner (Pantene). Only has food for the next day. ",
"Huggies diapers a box of 150 packs siz 5 & box of size 6 please. ",
"almond milk, rice, juice,meat,milk,wipes,diapers,pizza,cheese,toilet paper,cleaning aids,laundry soap/softener",
"Halal meat, chicken, fish, diapers, milk, watermelon, fruit, bananas apples avocados shampoos trash bag toilet paper soap shampoo detergent  tissue dish soap cereal tea bags water battles juice sodas ",
"REQUESTING $$ Cash App: 4252299103",
"I need a 800 or 1000 watt converter for my vehicle it's for charging my phone and lights and alarm clock you can pick them up $40 or $60 bucks at harbor. And I also need a batteries every size and some propane. And no cooking foods ",
"Dry food,diapers,always",
"REQUESTING $$ via cash app",
"Tomatoes, chayote (Mexican), sugar, salt, cinnamon stick, strawberries, banana, grapes, mandarins, bottles  water, rice, dried beans, laundry soap, dishwasher soap, conditioner for woman, toilet paper, towel paper, whole bread, olive oil, avocados, honey Cheerios cereal (no substitutes) - Family asked volunteer shop at Fred Meyer",
"Olive oil, toilet paper, gluten free snacks,water, mini cucumbers, tomatoes, avocado, watermelon, blueberry, melon, cottage cheese, paper towels, laundry soap, eggs, lemons, basmati rice, hand sanitizer ",
"Cracked wheat bread sliced ham bread and butter pickles tuna fish shredded cheese 2% milk veggies for salads fresh fruit (no apples) Raisin Bran crunch lucky charms frozen burritos or hot pockets chocolate chip cookies sour cream cheddar chips",
"Leche, wipes, frutas y verduras, azúcar, arroz y frijoles ",
"Sugar, salt, soy sauce, barbecue sauce, cilantro, jalapeno peppers, avocado, lemons, grapes, mayonnaise, menstrual pads, baby wipes, pullups size 3-4, toilet paper, bar soap, hand soap, dish soap, Clorox, toothpaste, chips ahoy cookies, hamburger meats, pork shoulder, pork ribs, tortillas.",
"Cracked wheat bread sliced ham bread and butter pickles tuna fish shredded cheese 2% milk veggies for salads fresh fruit (no apples) Raisin Bran crunch lucky charms frozen burritos or hot pockets chocolate chip cookies sour cream cheddar chips",
"Toallas femeninas",
"Similar pro-total comfort, Huggies diapers ",
"I will provide the list. I have Safeway vouchers from the school for $150 and I need someone to go to the store for me please. ",
"Tampons, chicken, Oranges wheat bread lemon strawberry ",
"Cracked wheat bread sliced ham bread and butter pickles tuna fish shredded cheese 2% milk veggies for salads fresh fruit (no apples) Raisin Bran crunch lucky charms frozen burritos or hot pockets chocolate chip cookies sour cream cheddar chips",
"Tomatoes, beef, regular pork, mayonnaise, cheese, toilet paper, laundry soap, dish soap, cookies, sugar, body soap, toothpaste,oil, instant coffee",
"Whole milk, pancake sausage on a stick, corn dogs, 18-24 pack of eggs, roast beef sandwich meat, meats-chicken, steak, pork, fish, blueberry pop tarts, family size cereal- Frosted Flakes, white bread, variety bags of chips, razors, body wash, 24 case of soda- coke ",
"Toiletries, purple overnight Always thin pads with wings , toilet paperS, detergent ,",
"Whole milk, pancake sausage on a stick, corn dogs, 18-24 pack of eggs, roast beef sandwich meat, meats-chicken, steak, pork, fish, blueberry pop tarts, family size cereal- Frosted Flakes, white bread, variety bags of chips, razors, body wash, 24 case of soda- coke ",
"Uncooked chicken (drumettes or thighs), Cracked wheat bread, sliced ham, bread and butter, pickles, tuna fish, shredded cheese, 2% milk, veggies for salads --romaine, cucumber, cherry tomatos, pepperoncini, fresh fruit (no apples), Raisin Bran crunch, lucky charms, frozen burritos or hot pockets, chocolate chip cookies, sour cream, cheddar chips (food is priority but Tide laundry detergent if in the budget)",
"Huevos, leche, frijoles, vegetales, fruta, pollo, papel de baño, pañales tamaño newborn para mi bebe que va a nacer pronto, ",
"Beef mince 4 lbs, Chicken breasts frozen 5 lb bag, chicken nuggets, juice V8 berry couple big bottles and orange, Jasmine Rice, salt, pepper, butter couple packages, eggs couple 18 packs, Vegetable oil 2 bottles, bottle white distilled vinegar. Toiletries; Toilet paper, paper towels, pantene shampoo and conditioner, body soap dove bar body soap big package, soft hand soap, Clorox wipes or spray, Playtex Sports pads(heavy flow please) Laundry; Tide washing liquid, downy in wash scent boosters.  Cascade platinum dishwasher Pods. ",
"I am not sure. I am filling this out on Adela's behalf. I am not Adela. I am a COVID-19 mutual aid Seattle grocery delivery volunteer and I received a call asking for support. Unfortunately, I am not able to make a delivery right now and I want to make sure that Adela's needs are met",
"Maquina para chequear la presion (automatic blood pressure monitor) - como en Walgreens",
"prioritize women's electric razor if possible! baby powder, deodorant, gallon of whole milk, salad greens/different kinds of salads",
"Meat-uncooked chicken or beef; lunch meat (turkey), sliced wheat or white bread, whole milk, any fruit- oranges, breakfast food -eggs and pancake batter, rice, noodles, bottled water, any veggies, toilet paper",
"Toilet paper, liquid body soap cares, hair shampoo and conditioner  for thick and damaged hair. , Dove or a Mitchum deodorant spray. Ginger ale , witch hazel or rose water for face cleaning , gain liquid laundry detergent , snuggles fabric softener , stuff to make s'mores with the kids for family of 4 . Match it charcoal the barbecue pit , beef Johnsonville hot links , beef hot dogs Oscar Mayer or ballpark , sweet relish , ketchup , mustard , best food mayonnaise , hot dog buns , family size Ruffles potato chips plain , watermelon . Rainier cherries , navel oranges , Dasani bottled waters , Dixie paper plates ,and cups , napkin , Bush's Baked Beans , skinless boneless salmon , fresh corn on the cob bicolor",
"Frozen chicken nuggets/strips, bread, waffles, any kind of cleaning supplies, wipes, hygiene products for adults and kids. Anything helps. ",
"crest 3d (artic fresh) toothpaste, eggs,  frozen entree items (such as chicken taquitos, pepperoni pizza, ham & cheese hot pockets or corn dogs),  frozen broccoli, frozen mixed veggies, chicken cups of noodle, spaghettios with franks or meatballs, whole milk, wheat bread, fresh fruit: peaches, grapes, strwaberries, watermelon, green or fuji apples.",
"Pads, shampoo, body wash, paper towels, oil, toilet paper, laundry soap, milk, sugar ",
"Pasta, rice, sugar, paper towel, toilet paper, organic vegetables: potatoes, tomatoes, onions, bell peppers, organic fruits: grapes, mangoes, papayas, apples, avocadoes, watermelon, water, whole milk, apple juice, chips"]

FOOD_RESTRICTIONS = ['Pork', 'Halal', 'Lactosa', 'All Nuts', 'None', 'None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','None','Peanuts','Milk, Pork', 'Milk', 'Alergy to sulfur', 'no pork at all', 'sour cream', 'allergy-peaches','oranges,apple cider','saseme seeds','halal meat only', 'vegetarian diet', 'no ninguna', 'no dairy','no meats, no veggies','alergic to water','coca cola','lactose intolerance']

SPECIAL_INFO = ["pacific island and european americans",
"Black ",
"Hispanic ",
"African American family with limited transportation and low money",
"U-visa, domestic violence survivor, autistic son, Spanish-speaker, health issues (recovering from dengue and cancer survivor)",
"Indijena",
"Soy indijena de guatemala",
"Arson, domestic",
"asylee, LatinX, DV survivor",
"Diverse household of color ",
"Hispanic",
"Person of color",
"African Americans (Muslims)",
"I can’t get to the store Rn ",
"Survivor of Domestic Violence",
"No",
"Black, recovering alcoholic, ",
"We are a Mexican family with 4 kids my husband and I are undocumented immigrants and not elegibles for unemployment or stimulus pay either ",
"Hispanic",
"LatinX, undocumented, latina, recovering from COVID-19. ",
"Hispanic",
"Hispanic ",
"Latino ",
"I am a black Muslim women with 3 children.",
"White, survivor of DV, disabled, PTSD",
"My family doesn't have any privileges. I don't qualify for government assistance. ",
"No",
"Single mother, undocumented, baby is 21 days old, has no support at home and clearly very exhausted!",
"Somalia ",
"Hispano ",
"We are an African family",
"We are an African family",
"My family and I are people of color. We would love help and support. ",
"Live in poor aparments",
"we are somali and no ",
"Hispanic ",
"By DNA I'm Spanish, native American but not registered as I don't know what tribe and I'm only 24% but I believe SW. "
"Black ",
"Hispanic",
"Unemployed at this moment",
"I can’t get to the store Rn ",
"I’m very limited and it’s hard to walk ",
"None",
"I’m very limited and it’s hard to walk ",
"Survivor of domestic violence",
"No violence ",
"No tengo privilegios y soy indijena",
"single mom",
"Black muslim family",
"I'm currently fleeing  I left my abuser April 6 of this year it's been a stuggle because I've been financially dependent so it's been scary not knowing  if we have enough food  for the day with my son and my self we are currently   in hiding from him trying to find safe permanent home ",
"African American",
"Im african American single mom with disabled autism  and his dad has passed away",
"Black",
"Immigrant, over 50 yrs old",
"Yes DV survivor, sexual violence, ",
"Latinos ",
"Latinos.  ",
"White , female ",
"Latinos ",
"Black",
"I am a survivor of domestic violence and a person of color. I am also disabled.",
"None",
"Black, African American ",
"Asian",
"multicultural woman currently divorcing, divorce has been pushed out and soon to be ex-husband was physically and financially abusive. No money or income",
"domestic violence survivor, LatinX, single mom",
"None ",
"Domestic violence ",
"Black-Somali Americans",
"person of color",
"No",
"Black",
"Person of color",
"I recently was just laid off of work and I am a domestic violence Survivor very little money and no resources",
"No ",
"Black",
"N/A",
"N/A",
"Black ",
"Black",
"African Americans (Muslims)",
"Black disabled 57yrs old with scholosis (curverty of the spinal cord and survivor of domestic violence",
"indigenous, LGBT",
"Single parent ",
"African American ",
"LatinX",
"black",
"no",
"We don't have any privileges. We can't get government assistance. ",
"Staying home mom ",
"Black",
"husband lost his job and difficult to support our family",
"Survivor of domestic violence,on section 8 housing,just lost job in march due to harassment.",
"LatinX, single mom",
"black",
"African Americans ",
"immigrant",
"Staying home mom ",
"I just moved in this apartment from being homeless. I'm a black single woman. Recovering from being homeless.",
"My family is black , we have 2 twins and 3 older kids 4 ,5 and 9 . No income at this time both parents laid off and struggling for help .",
"Single parent ",
"BIPOC",
"Indigenous single woman  with teenage sons",
"We are new to Washington ",
"No tenemos trabajo",
"Black",
"Muslim ",
"Undocumented Hispanic ineligible for unemployment aid.",
"Black",
"Single mother",
"No",
"Thank ",
"LatinX",
"Staying home mom ",
"White",
"N/A",
"N/A",
"Latinx",
"N/A",
"Asian /white ",
"N/A",
"Black",
"We are a muslim family of 7 with 5 kids and both my husband and I currently do not work.",
"I'm black and a senior citizen.",
"Indigena ",
"LatinX",
"Unemployed",
"Young African American mother of three sons one is compromised with having a heart condition so I’m home bound and I don’t have any money to do Instacart ",
"Staying home mom ",
"We are a Mexican family with 4 kids my husband and I are undocumented immigrants and not elegibles for unemployment or stimulus pay either ",
"I am Black single mother of 6",
"Black",
"I was raised by a very poor dysfunctional separated family and trying my best to keep my son and I above that! I have rheumatoid arthritis so just trying to stay healthy",
"LatinX",
"Black",
"Staying home mom ",
"AFRICAN AMERICAN",
"N/A",
"Former DV, LatinX, single mom ",
"African American, female. ",
"Single mom, LatinX",
"lost work in restaurant due to COVID",
"Etc...",
"Hispanic ",
"I am a latin gay and I don't have job for almost 3 months",
"Hispanic ",
"Staying home mom ",
"Black",
"LatinX",
"black",
"Elderly ",
"Both Elderly, one person in household is disabled ",
"Elderly, unable to leave home",
"Staying home mom ",
"Black and survivor of domestic violence, I'm on oxygen,sick and disabled and immune compromised.",
"Staying home mom ",
"African American",
"LatinX",
"Lost my job during this time, just moved to a rental house a few months ago ",
"Diverse household of color ",
"Staying home mom ",
"No are not",
"Greiving joblessness",
"Dv survivor single mom",
"Raza garífuna ",
"I am a bilingual person, Single mom of one baby! I am 21 years old. Currently not working, I don’t receive unemployment due to the slow process and the someone did a mistake on my application. I appeal but is taking more than one month! ",
"hispanic, husband black grandson mexican,  both disabled ",
"I live in Auburn, I'm african american single mother of 3 children, I feel as if other races that aren't black get more assistance.",
"Apartment complex",
"Domestic violence ",
"Dv survivor, sexual assault survivor, child abuse survivor, single mother ",
"Staying home mom ",
"Black ",
"Asylum seeker, Spanish speaking",
"Survivor of domestic violence", 
"Black and Pacific Islander ",
"Yess",
"LatinX, single mom, undocumented"
"Person of color",
"Somalia",]

LOCATIONS = [
    "Algona Pacific",
    "Auburn",
    "Bellevue",
    "Bothell",
    "Burien",
    "Carnation",
    "Covington",
    "Des Moines",
    "Duvall",
    "Fall City",
    "Federal Way",
    "High Line",
    "Issaquah",
    "Kenmore",
    "Kent",
    "Kirkland",
    "Maple Valley",
    "Newcastle",
    "Normandy Park",
    "North Bend",
    "Puyallup",
    "Redmond",
    "Renton",
    "Sammamish",
    "Snoqualmie",
    "Sumner",
    "Tukwila",
    "White Center",
    "Woodinville",
    "Sea Tac",
]

User = get_user_model()
def create_user(N):
    fake = Faker()
    for _ in range(N):
        first_name = fake.first_name()
        last_name = fake.last_name()
        is_volunteer = fake.pybool()
        is_requester = fake.pybool()
        email = fake.email()
        password = fake.password()
        display_name = "{}{}{}".format(first_name.lower(), last_name[0].lower(), random.choice([str(random.randint(1,99)),""]))
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_requester=is_requester,
            is_volunteer=is_volunteer,
            email=email,
            password=password, 
            display_name=display_name)

def create_request(N):
    fake = Faker()
    for _ in range(N):
        requester = random.choice(User.objects.filter(is_requester=True))
        phone = fake.phone_number()
        locations=random.choice(LOCATIONS)
        address1 = fake.address().split('\n')[0]
        address2 = fake.secondary_address()
        city = random.choice(CITY_CHOICES)[0]
        zip_code = fake.zipcode()
        contact_preference = random.choice(CONTACT_CHOICES)[0]
        agree_transfer = fake.pybool()
        prefered_food = random.choice(FOOD_CHOICES)[0]
        items_list = random.choice(GROCERY_LIST)
        food_restrictions = random.choice(FOOD_RESTRICTIONS)
        household_number = random.randint(1,8)
        urgency = random.choice(URGENCY_CHOICES)[0]
        financial_support = random.choice(FINANCIAL_SUPPORT_CHOICES)[0]
        special_info = random.choice(SPECIAL_INFO)
        share_info = random.choice(SHARE_INFO_CHOICES)[0]
        need_checkin = random.choice(NEED_CHECKIN_CHOICES)[0]
        extra_info = fake.text()
        ma_pod_setup = random.choice(MAPOD_SETUP_CHOICES)[0]
        offer_resources = fake.text()
        created_date = fake.date_time()
        status = random.choice(REQUEST_STATUS_CHOICES)[0]
        last_edit = "{}-{} by {} ".format(fake.month(),fake.day_of_month(),fake.first_name())
        locations = random.choice(LOCATIONS)
        Request.objects.create(requester=requester,phone=phone,address1=address1,address2=address2,
            city=city,zip_code=zip_code,contact_preference=contact_preference,
            prefered_food=prefered_food, items_list=items_list,food_restrictions=food_restrictions, household_number=household_number,
            urgency=urgency, financial_support=financial_support, special_info=special_info,share_info=share_info,need_checkin=need_checkin,
            extra_info=extra_info, ma_pod_setup=ma_pod_setup, offer_resources=offer_resources, created_date=created_date, status=status, last_edit=last_edit,
            agree_transfer=agree_transfer)

# def change_user():
#     for user in User.objects.all():
#         user.display_name = user.email.split('@')[0]
#         user.save()

create_user(100)
create_request(100)
# change_user()
print('Data is populated successfully!!')
