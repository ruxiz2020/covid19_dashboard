# flake8: noqa

# In[]:
# Controls for webapp
COUNTRIES = {
    "000": "Afghanistan",
    "001": "Albania",
    "002": "Algeria",
    "003": "Andorra",
    "004": "Angola",
    "005": "Anguilla",
    "006": "Antigua and Barbuda",
    "007": "Argentina",
    "008": "Armenia",
    "009": "Aruba",
    "010": "Australia",
    "011": "Austria",
    "012": "Azerbaijan",
    "013": "Bahamas",
    "014": "Bahrain",
    "015": "Bangladesh",
    "016": "Barbados",
    "017": "Belarus",
    "018": "Belgium",
    "019": "Belize",
    "020": "Benin",
    "021": "Bermuda",
    "022": "Bhutan",
    "023": "Bolivia",
    "024": "Bonaire Sint Eustatius and Saba",
    "025": "Bosnia and Herzegovina",
    "026": "Botswana",
    "027": "Brazil",
    "028": "British Virgin Islands",
    "029": "Brunei",
    "030": "Bulgaria",
    "031": "Burkina Faso",
    "032": "Burundi",
    "033": "Cambodia",
    "034": "Cameroon",
    "035": "Canada",
    "036": "Cape Verde",
    "037": "Cayman Islands",
    "038": "Central African Republic",
    "039": "Chad",
    "040": "Chile",
    "041": "China",
    "042": "Colombia",
    "043": "Comoros",
    "044": "Congo",
    "045": "Costa Rica",
    "046": "Cote d'Ivoire",
    "047": "Croatia",
    "048": "Cuba",
    "049": "Curacao",
    "050": "Cyprus",
    "051": "Czech Republic",
    "052": "Democratic Republic of Congo",
    "053": "Denmark",
    "054": "Djibouti",
    "055": "Dominica",
    "056": "Dominican Republic",
    "057": "Ecuador",
    "058": "Egypt",
    "059": "El Salvador",
    "060": "Equatorial Guinea",
    "061": "Eritrea",
    "062": "Estonia",
    "063": "Ethiopia",
    "064": "Faeroe Islands",
    "065": "Falkland Islands",
    "066": "Fiji",
    "067": "Finland",
    "068": "France",
    "069": "French Polynesia",
    "070": "Gabon",
    "071": "Gambia",
    "072": "Georgia",
    "073": "Germany",
    "074": "Ghana",
    "075": "Gibraltar",
    "076": "Greece",
    "077": "Greenland",
    "078": "Grenada",
    "079": "Guam",
    "080": "Guatemala",
    "081": "Guernsey",
    "082": "Guinea",
    "083": "Guinea-Bissau",
    "084": "Guyana",
    "085": "Haiti",
    "086": "Honduras",
    "087": "Hong Kong",
    "088": "Hungary",
    "089": "Iceland",
    "090": "India",
    "091": "Indonesia",
    "092": "Iran",
    "093": "Iraq",
    "094": "Ireland",
    "095": "Isle of Man",
    "096": "Israel",
    "097": "Italy",
    "098": "Jamaica",
    "099": "Japan",
    "100": "Jersey",
    "101": "Jordan",
    "102": "Kazakhstan",
    "103": "Kenya",
    "104": "Kosovo",
    "105": "Kuwait",
    "106": "Kyrgyzstan",
    "107": "Laos",
    "108": "Latvia",
    "109": "Lebanon",
    "110": "Lesotho",
    "111": "Liberia",
    "112": "Libya",
    "113": "Liechtenstein",
    "114": "Lithuania",
    "115": "Luxembourg",
    "116": "Macedonia",
    "117": "Madagascar",
    "118": "Malawi",
    "119": "Malaysia",
    "120": "Maldives",
    "121": "Mali",
    "122": "Malta",
    "123": "Mauritania",
    "124": "Mauritius",
    "125": "Mexico",
    "126": "Moldova",
    "127": "Monaco",
    "128": "Mongolia",
    "129": "Montenegro",
    "130": "Montserrat",
    "131": "Morocco",
    "132": "Mozambique",
    "133": "Myanmar",
    "134": "Namibia",
    "135": "Nepal",
    "136": "Netherlands",
    "137": "New Caledonia",
    "138": "New Zealand",
    "139": "Nicaragua",
    "140": "Niger",
    "141": "Nigeria",
    "142": "Northern Mariana Islands",
    "143": "Norway",
    "144": "Oman",
    "145": "Pakistan",
    "146": "Palestine",
    "147": "Panama",
    "148": "Papua New Guinea",
    "149": "Paraguay",
    "150": "Peru",
    "151": "Philippines",
    "152": "Poland",
    "153": "Portugal",
    "154": "Puerto Rico",
    "155": "Qatar",
    "156": "Romania",
    "157": "Russia",
    "158": "Rwanda",
    "159": "Saint Kitts and Nevis",
    "160": "Saint Lucia",
    "161": "Saint Vincent and the Grenadines",
    "162": "San Marino",
    "163": "Sao Tome and Principe",
    "164": "Saudi Arabia",
    "165": "Senegal",
    "166": "Serbia",
    "167": "Seychelles",
    "168": "Sierra Leone",
    "169": "Singapore",
    "170": "Sint Maarten (Dutch part)",
    "171": "Slovakia",
    "172": "Slovenia",
    "173": "Somalia",
    "174": "South Africa",
    "175": "South Korea",
    "176": "South Sudan",
    "177": "Spain",
    "178": "Sri Lanka",
    "179": "Sudan",
    "180": "Suriname",
    "181": "Swaziland",
    "182": "Sweden",
    "183": "Switzerland",
    "184": "Syria",
    "185": "Taiwan",
    "186": "Tajikistan",
    "187": "Tanzania",
    "188": "Thailand",
    "189": "Timor",
    "190": "Togo",
    "191": "Trinidad and Tobago",
    "192": "Tunisia",
    "193": "Turkey",
    "194": "Turks and Caicos Islands",
    "195": "Uganda",
    "196": "Ukraine",
    "197": "United Arab Emirates",
    "198": "United Kingdom",
    "199": "United States",
    "200": "United States Virgin Islands",
    "201": "Uruguay",
    "202": "Uzbekistan",
    "203": "Vatican",
    "204": "Venezuela",
    "205": "Vietnam",
    "206": "Western Sahara",
    "207": "Yemen",
    "208": "Zambia",
    "209": "Zimbabwe",
    "210": "World",
    "211": "International",
}

METRIC_TYPES = {
    "Total Cases": "total_cases",
    "New Cases": "new_cases",
    "Total Deaths": "total_deaths",
    "New Deaths": "new_deaths",
}

WELL_TYPES = dict(
    BR="Brine",
    Confidential="Confidential",
    DH="Dry Hole",
    DS="Disposal",
    DW="Dry Wildcat",
    GD="Gas Development",
    GE="Gas Extension",
    GW="Gas Wildcat",
    IG="Gas Injection",
    IW="Oil Injection",
    LP="Liquefied Petroleum Gas Storage",
    MB="Monitoring Brine",
    MM="Monitoring Miscellaneous",
    MS="Monitoring Storage",
    NL="Not Listed",
    OB="Observation Well",
    OD="Oil Development",
    OE="Oil Extension",
    OW="Oil Wildcat",
    SG="Stratigraphic",
    ST="Storage",
    TH="Geothermal",
    UN="Unknown",
)

COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)
