URGENCY_CHOICES = (
    ("In the next 72 hours", "In the next 72 hours"),
    ("Over the next few days", "Over the next few days"),
    ("Useful if available", "Useful if avaiable")
)
CONTACT_CHOICES = (
    ("Call","Phone Number - Call"),
    ("Text","Phone Number - Text"),
    ("Email", "Email")
)
CITY_CHOICES = (
    ("Algona Pacific","Algona Pacific"),
    ("Auburn","Auburn"),
    ("Bellevue","Bellevue"),
    ("Bothell","Bothell"),
    ("Burien","Burien"),
    ("Carnation","Carnation"),
    ("Covington","Covington"),
    ("Des Moines","Des Moines"),
    ("Duvall","Duvall"),
    ("Fall City","Fall City"),
    ("Federal Way","Federal Way"),
    ("High Line","High Line"),
    ("Issaquah","Issaquah"),
    ("Kenmore","Kenmore"),
    ("Kent","Kent"),
    ("Kirkland","Kirkland"),
    ("Maple Valley","Maple Valley"),
    ("Newcastle","Newcastle"),
    ("Normandy Park","Normandy Park"),
    ("North Bend","North Bend"),
    ("Puyallup","Puyallup"),
    ("Redmond","Redmond"),
    ("Renton","Renton"),
    ("Sammamish","Sammamish"),
    ("SeaTac","SeaTac"),
    ("Snoqualmie","Snoqualmie"),
    ("Sumner","Sumner"),
    ("Tukwila","Tukwila"),
    ("White Center","White Center"),
    ("Woodinville","Woodinville"),
)

FOOD_CHOICES = (
    ("Ingredients to cook with","Cook"),
    ("Reheat and serve/frozen","Reheat"),
    ("Low Prep (like sandwiches, pasta)","Low-Prep"),
    ("Zero - Prep","Instant"),
)

FINANCIAL_SUPPORT_CHOICES = (
    ("Self-Pay and Donate", "Pay with your own money and donate to support your community members"),
    ("Self-Pay", "Pay with your own money (coordinate with delivery person)"),
    ("Request Support", "Request support with your delivery items"),
)
SHARE_INFO_CHOICES = (
    (True,"Yes"),
    (False,"No")
)

NEED_CHECKIN_CHOICES = (
    ("Text","Yes, by text"),
    ("Phone","Yes, by phone"),
    ("No","No, thank you"),
)
MAPOD_SETUP_CHOICES = (
    (True,"Yes"),
    (False,"No")
)

AGREE_TRANSFER_CHOICES = (
    (True,"Yes"),
    (False,"No")
)

REQUEST_STATUS_CHOICES = (
    ("New", "New"),
    ("Pending","Pending"),
    ("In Process","In Process"),
    ("Completed","Completed"),
    ("Transferred","Transferred"),
)

VOLUNTEER_STATUS_CHOICES = (
    ('Available','Available'),
    ('Unavailable', 'Unavailable')
)

VOLUNTEERING_STATUS_SIGNED_UP = 'Signed Up'
VOLUNTEERING_STATUS_READY = 'Ready'
VOLUNTEERING_STATUS_DELIVERED = 'Delivered'
VOLUNTEERING_STATUS_OTW = 'On the way'

VOLUNTEERING_STATUS_CHOICES = (
    (VOLUNTEERING_STATUS_SIGNED_UP, 'Signed Up'),
    (VOLUNTEERING_STATUS_READY, 'Ready'),
    (VOLUNTEERING_STATUS_DELIVERED, 'Delivered')
)