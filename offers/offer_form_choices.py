
CONTACT_CHOICES = (
    ("Call", "Phone Number - Call"),
    ("Text", "Phone Number - Text"),
    ("Email", "Email")
)
CITY_CHOICES = (
    ("Algona Pacific", "Algona Pacific"),
    ("Auburn", "Auburn"),
    ("Bellevue", "Bellevue"),
    ("Bothell", "Bothell"),
    ("Burien", "Burien"),
    ("Carnation", "Carnation"),
    ("Covington", "Covington"),
    ("Des Moines", "Des Moines"),
    ("Duvall", "Duvall"),
    ("Fall City", "Fall City"),
    ("Federal Way", "Federal Way"),
    ("High Line", "High Line"),
    ("Issaquah", "Issaquah"),
    ("Kenmore", "Kenmore"),
    ("Kent", "Kent"),
    ("Kirkland", "Kirkland"),
    ("Maple Valley", "Maple Valley"),
    ("Newcastle", "Newcastle"),
    ("Normandy Park", "Normandy Park"),
    ("North Bend", "North Bend"),
    ("Puyallup", "Puyallup"),
    ("Redmond", "Redmond"),
    ("Renton", "Renton"),
    ("Sammamish", "Sammamish"),
    ("SeaTac", "SeaTac"),
    ("Snoqualmie", "Snoqualmie"),
    ("Sumner", "Sumner"),
    ("Tukwila", "Tukwila"),
    ("White Center", "White Center"),
    ("Woodinville", "Woodinville"),
)

ACCESSIBILITY_NEEDS_CHOICES = (
    (
        'A buddy to do delivers with',
        'A buddy to do delivers with'
    ),
    (
        'Help acquiring hand sanitizer/wipes',
        'Help acquiring hand sanitizer/wipes'
    ),
    ('Other',  'Other')
)


FINANCIAL_SUPPORT_CHOICES = (
    ("Money Upfront", "No. I will need money ahead of time in order to buy the groceries."),
    ("Self-Pay, Need Reimbursement",
     "No. I have the money to make the initial purchase, but I will need reimbursement."),
    ("Self-Pay, Partially Donate",
     "Yes. I have the money to make the initial purchase & can donate some, but I may need reimbursement eventually."),
    ("Donate All", "Yes. I will donate any groceries I pick up."),
    ("Other", "Ohter"),
)

NEED_CHECKIN_CHOICES = (
    ('Text, 2-3 weeks', 'check-in via text once every 2-3 weeks'),
    ('Text, once a month', 'check-in via text once a month'),
    ('Phone, 2-3 weeks', 'check-in via phone once every 2-3 weeks'),
    ('Phone, once a month', 'check-in via phone once a month'),
    ('Other', 'Other'),
)
MAPOD_SETUP_CHOICES = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("Other", "Other"),
)

AVAILABILITY_CHOICES = (
    ('Mornings', 'Mornings'),
    ('Afternoons', 'Afternoons'),
    ('Evening', 'Evening'),
    ('Weekends', 'Weekends'),
    ('Other', 'Other')
)


COORDINATING_CHOICES = (
    ('6hrs/weeks 2hrs/weeks 3months',
     'Commit at least 6 hours per week for the first few weeks and then 2 hours or more after for at least three months'),
    ('Be willing to learn or take training', 'Have an understanding or be willing to learn about transformative justice, abolition, solidarity support, emotional first aid, or take these necessary training within the first couple of weeks of volunteering'),
    ('Attend weekly meetings and be committed',
     'Attend weekly meetings and be committed to continued learning and struggle'),
    ('Other', 'Other'),
)
