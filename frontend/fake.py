masterProducts = [
    {
        "id": 1,
        "title": "Amazing Product",
        "url": "https://example.com/product/1",
        "description": "This is a fantastic product that will change your life.",
        "features": "Feature 1|Feature 2|Feature 3",
        "content": "{\"key1\": \"value1\", \"key2\": \"value2\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 2,
        "title": "Supercharged Gadget",
        "url": "https://example.com/gadget/2",
        "description": "The ultimate tool for productivity and entertainment.",
        "features": "High-speed processor|Long battery life|Crystal clear display",
        "content": "{\"performance\": \"excellent\", \"battery\": \"long-lasting\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 3,
        "title": "Cozy Comfort Blanket",
        "url": "https://example.com/blanket/3",
        "description": "Wrap yourself in pure luxury and ultimate comfort.",
        "features": "Ultra-soft material|Warm and breathable|Machine washable",
        "content": "{\"material\": \"plush\", \"temperature\": \"warm\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 4,
        "title": "Smart Home Speaker",
        "url": "https://example.com/speaker/4",
        "description": "Control your smart home with just your voice.",
        "features": "Voice assistant integration|Multiple streaming services|Multi-room audio",
        "content": "{\"capabilities\": \"voice control, music streaming\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 5,
        "title": "Travel-Friendly Water Bottle",
        "url": "https://example.com/bottle/5",
        "description": "Stay hydrated on the go with this leak-proof and stylish bottle.",
        "features": "Double-walled insulation|Leak-proof lid|Durable construction",
        "content": "{\"insulation\": \"double-walled\", \"leakproof\": \"true\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 6,
        "title": "Noise-Cancelling Headphones",
        "url": "https://example.com/headphones/6",
        "description": "Immerse yourself in your music without distractions.",
        "features": "Active noise cancellation|Superior sound quality|Comfortable fit",
        "content": "{\"noise_cancellation\": \"active\", \"sound_quality\": \"superior\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 7,
        "title": "Fitness Tracker",
        "url": "https://example.com/tracker/7",
        "description": "Track your workouts and progress towards your fitness goals.",
        "features": "Step tracking|Heart rate monitoring|Sleep analysis",
        "content": "{\"functions\": \"step tracking, heart rate monitoring\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
    {
        "id": 8,
        "title": "Portable Projector",
        "url": "https://example.com/projector/8",
        "description": "Bring the big screen experience anywhere you go.",
        "features": "High-definition picture|Portable and lightweight|Long-lasting battery",
        "content": "{\"resolution\": \"high-definition\", \"portability\": \"high\"}",
        "created_at": "2024-05-13T14:57:00Z"
    },
]

local_master = [
    {
        "title": "Local Amazing Product",
        "url": "https://example.com/product/1",
        "content_params": {
            "key1": "value1",
            "key2": "value2"
        }
    },
    {
        "title": "Supercharged Gadget",
        "url": "https://example.com/gadget/2",
        "content_params": {
            "performance": "excellent",
            "battery": "long-lasting"
        }
    },
    {
        "title": "Cozy Comfort Blanket",
        "url": "https://example.com/blanket/3",
        "content_params": {
            "material": "plush",
            "temperature": "warm"
        }
    },
    # Add more products as needed
]

product = [
    {
        "title": "Nexans H07V-U",
        "url": "https://www.nexans.fr/en/products/Building/Residential/Rigides-Wires/H07V-U-536932466.html",
        "description": "Conductors without external sheath, PVC insulation, for general use",
        "images": [
            "/.rest/eservice/dam/v1/image/258917?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/258590?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/255502?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/247027?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/262509?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/258917?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/258590?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/255502?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/247027?variant=856x856&scaleType=FILL",
            "/.rest/eservice/dam/v1/image/262509?variant=856x856&scaleType=FILL"
        ],
        "downloads": [
            {
                "title": "Datasheet",
                "data": "PDF",
                "link": "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10255290"
            }
        ],
        "description_details": {
            "norms": [
                {
                    "International": "EN 50525-2-31; HD 21.3; IEC 60227-1"
                },
                {
                    "National": "NF C32-201/3"
                }
            ],
            "Application": "Nexans H07V-U conductors are used for fixed protected installations : i.e. ligths or control gear (from offices, domestic or commercial buildings ...) with voltage ≤ 1000V AC or ≤ 750 V DC . ...",
            "Installation": "Open air, in conduit, in cable trunking, in cable ducting. Thanks to the sliding properties of insulation, H07V-U is made to facilitate processing while pulling in.",
            "Design": "",
            "Marking": "S.Y + USE «har» H07V-U factory number",
            "Voltage drop": "Calculated with Cos phi = 0,8"
        },
        "characteristics": {
            "Conductor flexibility": "Solid class 1",
            "Conductor material": "Bare copper",
            "Conductor shape": "Circular",
            "Insulation": "PVC",
            "Lead free": "Yes",
            "Rated Voltage Uo/U (Um)": "450/750 V",
            "Mechanical resistance to impacts": "Low",
            "Flame retardant": "-",
            "Max. conductor temperature in service": "70 °C",
            "Short-circuit max. conductor temperature": "160 °C",
            "Operating temperature, range": "-5 ... 60 °C",
            "Weather resistance": "No",
            "Chemical resistance": "Accidental",
            "Water proof": "Low"
        },
        "resources": [
            {
                "title": "Licence H07V-U",
                "link": "https://www.nexans.fr/.rest/eservice/dam/v1/file/223556/Licence H07V-U  644666A1_3.pdf",
                "file_info": "pdf — 66.3 kB"
            },
            {
                "title": "PEP ECOPASSPORT H07V-U ECA",
                "link": "https://www.nexans.fr/.rest/eservice/dam/v1/file/251628/PEP ECOPASSPORT H07V-U ECA.pdf",
                "file_info": "pdf — 5.1 MB"
            },
            {
                "title": "CMC PASSEO VU",
                "link": "https://www.nexans.fr/.rest/eservice/dam/v1/file/262150/CMC passeo H07VU.pdf",
                "file_info": "pdf — 250.3 kB"
            },
            {
                "title": "CMC H07V-U",
                "link": "https://www.nexans.fr/.rest/eservice/dam/v1/file/262151/CMC H07VU.pdf",
                "file_info": "pdf — 237.3 kB"
            },
            {
                "title": "Brochure gamme 2024",
                "link": "https://www.nexans.fr/.rest/eservice/dam/v1/file/262221/BROCHURE GAMME 2024 1_4.pdf",
                "file_info": "pdf — 3.1 MB"
            }
        ],
        "variants": [
            {
                "title": "Nexans 3xVU 1,5  BLUE-BLACK-GREEN/YELLOW",
                "reference": "Nexans ref. 10255290",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "-",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10255290"
                ]
            },
            {
                "title": "Nexans 3xVU 1,5 2 BLUE-BLACK-GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10255293",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "-",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10255293"
                ]
            },
            {
                "title": "Nexans ASSEMBLE 3 fils VU1,5 C30m",
                "reference": "Nexans ref. 10202735",
                "specs": {
                    "packaging": "Coil (30m)",
                    "colorsh": "-",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "30"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10202735"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK C5m",
                "reference": "Nexans ref. 10026438",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026438"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK C5m",
                "reference": "Nexans ref. 10136302",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10136302"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK BOB 5m",
                "reference": "Nexans ref. 10026436",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026436"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK C10m",
                "reference": "Nexans ref. 10026473",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026473"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK",
                "reference": "Nexans ref. 10097337",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097337"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK BOB 10m",
                "reference": "Nexans ref. 10026471",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026471"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 BLACK C25m",
                "reference": "Nexans ref. 10026545",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026545"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK C25m",
                "reference": "Nexans ref. 10207975",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10207975"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK BOB 25m",
                "reference": "Nexans ref. 10026543",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026543"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 7 BLACK C75m",
                "reference": "Nexans ref. 10253802",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253802"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLACK  C100m",
                "reference": "Nexans ref. 10026378",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026378"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 BLACK C100m",
                "reference": "Nexans ref. 10269978 - Country ref. 01225015",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269978"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 BLACK C750m",
                "reference": "Nexans ref. 10124399 - Country ref. 01270348",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124399"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 BLACK",
                "reference": "Nexans ref. 10241389",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Black",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241389"
                ]
            },
            {
                "title": "Nexans H07VU 1X1,5  BLUE C5m",
                "reference": "Nexans ref. 10026427",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026427"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE C5m",
                "reference": "Nexans ref. 10026433",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026433"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE C5m",
                "reference": "Nexans ref. 10097272",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097272"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE BOB 5m",
                "reference": "Nexans ref. 10026431",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026431"
                ]
            },
            {
                "title": "Nexans H07VU 1X1,5  BLUE C10m",
                "reference": "Nexans ref. 10026463",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026463"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE",
                "reference": "Nexans ref. 10097293",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097293"
                ]
            },
            {
                "title": "Nexans H07VU 1X1,5  BLUE C10m",
                "reference": "Nexans ref. 10026450",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026450"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE  BOB 10m",
                "reference": "Nexans ref. 10026460",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026460"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE C25m",
                "reference": "Nexans ref. 10026536",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026536"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 BLUE C25m",
                "reference": "Nexans ref. 10097270",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097270"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE BOB 25m",
                "reference": "Nexans ref. 10026534",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026534"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 7 BLUE C75m",
                "reference": "Nexans ref. 10253801",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253801"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE  C100m",
                "reference": "Nexans ref. 10026372",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026372"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 BLUE C100m",
                "reference": "Nexans ref. 10269975 - Country ref. 01225017",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269975"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE C100m",
                "reference": "Nexans ref. 10225996",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10225996"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BLUE C50m",
                "reference": "Nexans ref. 10243643",
                "specs": {
                    "packaging": "Coil (50m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10243643"
                ]
            },
            {
                "title": "Nexans H07VU-1,5-BLUE C100m",
                "reference": "Nexans ref. 10274808",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274808"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 BLUE C500m",
                "reference": "Nexans ref. 10043637",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043637"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 BLUE C750m",
                "reference": "Nexans ref. 10124400 - Country ref. 01270349",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124400"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 BLUE",
                "reference": "Nexans ref. 10239885",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10239885"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 light  BLUE",
                "reference": "Nexans ref. 10269617",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269617"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BROWN C5m",
                "reference": "Nexans ref. 10130801",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10130801"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BROWN C10m",
                "reference": "Nexans ref. 10026470",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026470"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 BROWN C25m",
                "reference": "Nexans ref. 10026542",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026542"
                ]
            },
            {
                "title": "Nexans H07VU-1,5-GREEN/YELLOW BOB 25m",
                "reference": "Nexans ref. 10274809",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274809"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 7 BROWN C75m",
                "reference": "Nexans ref. 10253803",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253803"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  BROWN  C100m",
                "reference": "Nexans ref. 10026376",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026376"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 BROWN C100m",
                "reference": "Nexans ref. 10269976 - Country ref. 01225016",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269976"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 BROWN C500m",
                "reference": "Nexans ref. 10043638",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043638"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 BROWN C750m",
                "reference": "Nexans ref. 10124401 - Country ref. 01270350",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124401"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 BROWN",
                "reference": "Nexans ref. 10241388",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Brown",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241388"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 DARK BLUE C500m",
                "reference": "Nexans ref. 10140205",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Dark blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10140205"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 DARK BLUE C750m",
                "reference": "Nexans ref. 10140149 - Country ref. 01270389",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Dark blue",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10140149"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW C5m",
                "reference": "Nexans ref. 10026446",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026446"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW C5m",
                "reference": "Nexans ref. 10097291",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097291"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW BOB 5m",
                "reference": "Nexans ref. 10026444",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026444"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW C10m",
                "reference": "Nexans ref. 10026489",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026489"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW",
                "reference": "Nexans ref. 10097299",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097299"
                ]
            },
            {
                "title": "Nexans HO7VU 1X1,5  GREEN/YELLOW C10m",
                "reference": "Nexans ref. 10026453",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026453"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW BOB 10m",
                "reference": "Nexans ref. 10026486",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026486"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10026556",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026556"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10097307",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097307"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 GREEN/YELLOW BOB 25m",
                "reference": "Nexans ref. 10026554",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026554"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW C50m",
                "reference": "Nexans ref. 10243695",
                "specs": {
                    "packaging": "Coil (50m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "50"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10243695"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 7 GREEN/YELLOW C75m",
                "reference": "Nexans ref. 10253834",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253834"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW  C100m",
                "reference": "Nexans ref. 10026374",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026374"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1G1.5 GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10269963 - Country ref. 01225010",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269963"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10225997",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10225997"
                ]
            },
            {
                "title": "Nexans H07VU-1,5-BROWN C100m",
                "reference": "Nexans ref. 10274807",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274807"
                ]
            },
            {
                "title": "Nexans H07VU-1,5-GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10274810",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274810"
                ]
            },
            {
                "title": "Nexans H07V-U 1G1.5 GREEN/YELLOW C750m",
                "reference": "Nexans ref. 10124398 - Country ref. 01270347",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124398"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 GREEN/YELLOW",
                "reference": "Nexans ref. 10241393",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Green / Yellow",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241393"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 GREY C100m",
                "reference": "Nexans ref. 10269977 - Country ref. 01248685",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Grey",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269977"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 GREY C750m",
                "reference": "Nexans ref. 10124418 - Country ref. 01270355",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Grey",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124418"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 GREY",
                "reference": "Nexans ref. 10256005",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Grey",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10256005"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 IVORY C100m",
                "reference": "Nexans ref. 10269974",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Ivory",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269974"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 IVORY C500m",
                "reference": "Nexans ref. 10043646",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Ivory",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043646"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 IVORY C750m",
                "reference": "Nexans ref. 10124417 - Country ref. 01270354",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Ivory",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124417"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 IVORY",
                "reference": "Nexans ref. 10256006",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Ivory",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10256006"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  ORANGE C5m",
                "reference": "Nexans ref. 10130799",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10130799"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  ORANGE C10m",
                "reference": "Nexans ref. 10026468",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026468"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 ORANGE C25m",
                "reference": "Nexans ref. 10026540",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026540"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  ORANGE  C100m",
                "reference": "Nexans ref. 10026380",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026380"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 ORANGE C100m",
                "reference": "Nexans ref. 10269979 - Country ref. 01225013",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269979"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 Orange C750m",
                "reference": "Nexans ref. 10124416 - Country ref. 01270353",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124416"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 ORANGE",
                "reference": "Nexans ref. 10241740",
                "specs": {
                    "packaging": "Box (1458m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "1458"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241740"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 ORANGE",
                "reference": "Nexans ref. 10241390",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Orange",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241390"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 PURPLE C100m",
                "reference": "Nexans ref. 10269981 - Country ref. 01225012",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Purple",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269981"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED C5m",
                "reference": "Nexans ref. 10026442",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026442"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED C5m",
                "reference": "Nexans ref. 10097289",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097289"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED BOB 5m",
                "reference": "Nexans ref. 10026440",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026440"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED C10m",
                "reference": "Nexans ref. 10026481",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026481"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED",
                "reference": "Nexans ref. 10097297",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097297"
                ]
            },
            {
                "title": "Nexans HO7VU 1X1,5  RED C10m",
                "reference": "Nexans ref. 10026458",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026458"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED BOB 10m",
                "reference": "Nexans ref. 10026478",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026478"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 RED C25m",
                "reference": "Nexans ref. 10026551",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026551"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 RED C25m",
                "reference": "Nexans ref. 10097304",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097304"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 RED BOB 25m",
                "reference": "Nexans ref. 10026549",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026549"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED C50m",
                "reference": "Nexans ref. 10243694",
                "specs": {
                    "packaging": "Coil (50m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "50"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10243694"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED  C100m",
                "reference": "Nexans ref. 10026382",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026382"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X1.5 RED C100m",
                "reference": "Nexans ref. 10269980 - Country ref. 01225011",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269980"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED C100m",
                "reference": "Nexans ref. 10225995",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10225995"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 RED C500m",
                "reference": "Nexans ref. 10043640",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043640"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 RED C750m",
                "reference": "Nexans ref. 10124403 - Country ref. 01270351",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124403"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 RED",
                "reference": "Nexans ref. 10241391",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Red",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241391"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 1,5 C5m",
                "reference": "Nexans ref. 10026402",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026402"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 1,5 C10m",
                "reference": "Nexans ref. 10026404",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026404"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 1,5",
                "reference": "Nexans ref. 10199401",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "3",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10199401"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 1,5 C25m",
                "reference": "Nexans ref. 10050579",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10050579"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 1,5 C25m",
                "reference": "Nexans ref. 10199399",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "3",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10199399"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 FILS 1.5 C25m",
                "reference": "Nexans ref. 10262687",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "1.5",
                    "nbcores": "3",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10262687"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE C5m",
                "reference": "Nexans ref. 10130800",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10130800"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE C5m",
                "reference": "Nexans ref. 10207976",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10207976"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE C10m",
                "reference": "Nexans ref. 10026476",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026476"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE",
                "reference": "Nexans ref. 10207978",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10207978"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5 PURPLE C25m",
                "reference": "Nexans ref. 10026548",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026548"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE C25m",
                "reference": "Nexans ref. 10207979",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10207979"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  PURPLE C100m",
                "reference": "Nexans ref. 10026384",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026384"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 PURPLE C500m",
                "reference": "Nexans ref. 10043642",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043642"
                ]
            },
            {
                "title": "Nexans H07VU 1x1,5  RED  C500m",
                "reference": "Nexans ref. 10026430",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026430"
                ]
            },
            {
                "title": "Nexans H07V-U 1x1.5 PURPLE C750m",
                "reference": "Nexans ref. 10124414 - Country ref. 01270352",
                "specs": {
                    "packaging": "Coil (750m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "750"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10124414"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x1,5 PURPLE",
                "reference": "Nexans ref. 10241392",
                "specs": {
                    "packaging": "Box (2900m)",
                    "colorsh": "Violet",
                    "section": "1.5",
                    "nbcores": "1",
                    "length": "2900"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241392"
                ]
            },
            {
                "title": "Nexans 3xVU 2,5  BLUE-BLACK-GREEN/YELLOW",
                "reference": "Nexans ref. 10255291",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "-",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10255291"
                ]
            },
            {
                "title": "Nexans 3xVU 2,5 2 BLUE-BLACK-GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10255364",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "-",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10255364"
                ]
            },
            {
                "title": "Nexans ASSEMBLE 3 fils VU2,5 C30m",
                "reference": "Nexans ref. 10202736",
                "specs": {
                    "packaging": "Coil (30m)",
                    "colorsh": "-",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "30"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10202736"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLACK BOB 5m",
                "reference": "Nexans ref. 10026415",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026415"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLACK C10m",
                "reference": "Nexans ref. 10028622",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10028622"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLACK BOB 10m",
                "reference": "Nexans ref. 10026510",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026510"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLACK C25m",
                "reference": "Nexans ref. 10026574",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026574"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 BLACK C25m",
                "reference": "Nexans ref. 10028630",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10028630"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 BLACK BOB 25m",
                "reference": "Nexans ref. 10026572",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026572"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 7 BLACK C75m",
                "reference": "Nexans ref. 10253836",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253836"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLACK C100m",
                "reference": "Nexans ref. 10026391",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026391"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 BLACK C100m",
                "reference": "Nexans ref. 10269985 - Country ref. 01225055",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269985"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 BLACK C500m",
                "reference": "Nexans ref. 10043649 - Country ref. 01225075",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043649"
                ]
            },
            {
                "title": "Nexans H07VU 1X2,5 500m BLACK C500m",
                "reference": "Nexans ref. 10027875",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10027875"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 BLACK",
                "reference": "Nexans ref. 10241429",
                "specs": {
                    "packaging": "Box (866m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "833"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241429"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 BLACK",
                "reference": "Nexans ref. 10241425",
                "specs": {
                    "packaging": "Box (1600m)",
                    "colorsh": "Black",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "1600"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241425"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C5m",
                "reference": "Nexans ref. 10026413",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026413"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C5m",
                "reference": "Nexans ref. 10097313",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097313"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE BOB 5m",
                "reference": "Nexans ref. 10026411",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026411"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C10m",
                "reference": "Nexans ref. 10026506",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026506"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE",
                "reference": "Nexans ref. 10216107",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10216107"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE",
                "reference": "Nexans ref. 10097315",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097315"
                ]
            },
            {
                "title": "Nexans H07VU 1X2,5  BLUE C10m",
                "reference": "Nexans ref. 10026495",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026495"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE BOB 10m",
                "reference": "Nexans ref. 10026503",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026503"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 BLUE C25m",
                "reference": "Nexans ref. 10026569",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026569"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C25m",
                "reference": "Nexans ref. 10097338",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097338"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 BLUE BOB 25m",
                "reference": "Nexans ref. 10026567",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026567"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 7 BLUE C75m",
                "reference": "Nexans ref. 10253835",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253835"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C100m",
                "reference": "Nexans ref. 10026386",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026386"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 BLUE C100m",
                "reference": "Nexans ref. 10269983 - Country ref. 01225057",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269983"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BLUE C100m",
                "reference": "Nexans ref. 10225999",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10225999"
                ]
            },
            {
                "title": "Nexans H07VU-2,5-BLEU C100m",
                "reference": "Nexans ref. 10274812",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274812"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 BLUE C500m",
                "reference": "Nexans ref. 10043650 - Country ref. 01225077",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043650"
                ]
            },
            {
                "title": "Nexans H07VU 1X2,5 500m BLUE C500m",
                "reference": "Nexans ref. 10027868",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10027868"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 BLUE",
                "reference": "Nexans ref. 10239886",
                "specs": {
                    "packaging": "Box (1600m)",
                    "colorsh": "Blue",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "1600"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10239886"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BROWN C10m",
                "reference": "Nexans ref. 10028623",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/prodt/pdf/10028623"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 BROWN C25m",
                "reference": "Nexans ref. 10171284",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10171284"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 7 BROWN C75m",
                "reference": "Nexans ref. 10253837",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253837"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  BROWN C100m",
                "reference": "Nexans ref. 10058059",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10058059"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 BROWN C100m",
                "reference": "Nexans ref. 10269984 - Country ref. 01225056",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269984"
                ]
            },
            {
                "title": "Nexans H07VU-2,5-BROWN C100m",
                "reference": "Nexans ref. 10274811",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274811"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 BROWN C500m",
                "reference": "Nexans ref. 10043651 - Country ref. 01225076",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043651"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 BROWN",
                "reference": "Nexans ref. 10241428",
                "specs": {
                    "packaging": "Box (833m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "833"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241428"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 BROWN",
                "reference": "Nexans ref. 10241424",
                "specs": {
                    "packaging": "Box (1600m)",
                    "colorsh": "Brown",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "1600"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241424"
                ]
            },
            {
                "title": "Nexans H07VU 1X1,5  GREEN/YELLOW C5m",
                "reference": "Nexans ref. 10026428",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026428"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C5m",
                "reference": "Nexans ref. 10026425",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026425"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C5m",
                "reference": "Nexans ref. 10097311",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097311"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW BOB 5m",
                "reference": "Nexans ref. 10026423",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026423"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C10m",
                "reference": "Nexans ref. 10026526",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026526"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW",
                "reference": "Nexans ref. 10097336",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097336"
                ]
            },
            {
                "title": "Nexans H07VU 1X2,5  GREEN/YELLOW C10m",
                "reference": "Nexans ref. 10026498",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026498"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW BOB 10m",
                "reference": "Nexans ref. 10026523",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026523"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10026583",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026583"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10097341",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097341"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW BOB 25m",
                "reference": "Nexans ref. 10026581",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026581"
                ]
            },
            {
                "title": "Nexans H07VU-2,5-GREEN/YELLOW BOB 25m",
                "reference": "Nexans ref. 10274813",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274813"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 7 GREEN/YELLOW C75m",
                "reference": "Nexans ref. 10253838",
                "specs": {
                    "packaging": "Coil (75m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "75"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10253838"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10026388",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026388"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1G2.5 GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10269982",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269982"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10026389",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026389"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10226000",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10226000"
                ]
            },
            {
                "title": "Nexans H07VU-2,5-GREEN/YELLOW C100m",
                "reference": "Nexans ref. 10274834",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274834"
                ]
            },
            {
                "title": "Nexans H07V-U 1G2.5 GREEN/YELLOW C500m",
                "reference": "Nexans ref. 10043648 - Country ref. 01225070",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043648"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 GREEN/YELLOW",
                "reference": "Nexans ref. 10241426",
                "specs": {
                    "packaging": "Box (1600m)",
                    "colorsh": "Green / Yellow",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "1600"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241426"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 GREY C500m",
                "reference": "Nexans ref. 10043627",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Grey",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043627"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 IVORY C500m",
                "reference": "Nexans ref. 10043625",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Ivory White - RAL 1015",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043625"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 ORANGE C100m",
                "reference": "Nexans ref. 10269986",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Orange",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269986"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  ORANGE C100m",
                "reference": "Nexans ref. 10026393",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Orange",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026393"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 Orange C500m",
                "reference": "Nexans ref. 10043748 - Country ref. 01225073",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Orange",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043748"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 PURPLE C100m",
                "reference": "Nexans ref. 10269949",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Purple",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269949"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C5m",
                "reference": "Nexans ref. 10026421",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026421"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C5m",
                "reference": "Nexans ref. 10097308",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097308"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED BOB 5m",
                "reference": "Nexans ref. 10026419",
                "specs": {
                    "packaging": "Spool (5m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026419"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C10m",
                "reference": "Nexans ref. 10026518",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026518"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED",
                "reference": "Nexans ref. 10216106",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10216106"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED",
                "reference": "Nexans ref. 10097322",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097322"
                ]
            },
            {
                "title": "Nexans H07VU 1X2,5  RED C10m",
                "reference": "Nexans ref. 10026501",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026501"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED BOB 10m",
                "reference": "Nexans ref. 10026515",
                "specs": {
                    "packaging": "Spool (10m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026515"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 RED C25m",
                "reference": "Nexans ref. 10026578",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026578"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C25m",
                "reference": "Nexans ref. 10097340",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10097340"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED BOB 25m",
                "reference": "Nexans ref. 10026576",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026576"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5 RED BOB 25m",
                "reference": "Nexans ref. 10028631",
                "specs": {
                    "packaging": "Spool (25m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10028631"
                ]
            },
            {
                "title": "Nexans H07V-U PASSEO 1X2.5 RED C100m",
                "reference": "Nexans ref. 10269948 - Country ref. 01225051",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10269948"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C100m",
                "reference": "Nexans ref. 10026394",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026394"
                ]
            },
            {
                "title": "Nexans H07VU 1x2,5  RED C100m",
                "reference": "Nexans ref. 10225998",
                "specs": {
                    "packaging": "Coil (100m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "100"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10225998"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 RED C500m",
                "reference": "Nexans ref. 10043652 - Country ref. 01225071",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043652"
                ]
            },
            {
                "title": "Nexans EASYBOX H07VU 1x2,5 RED",
                "reference": "Nexans ref. 10241427",
                "specs": {
                    "packaging": "Box (1600m)",
                    "colorsh": "Red",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "1600"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10241427"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 2,5 C5m",
                "reference": "Nexans ref. 10026617",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026617"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 FILS 2.5 C5m",
                "reference": "Nexans ref. 10262690",
                "specs": {
                    "packaging": "Coil (5m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "3",
                    "length": "5"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10262690"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 2,5 C10m",
                "reference": "Nexans ref. 10026630",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10026630"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 2,5",
                "reference": "Nexans ref. 10199402",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "3",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10199402"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 FILS 2.5",
                "reference": "Nexans ref. 10262688",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "3",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10262688"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 2,5 C25m",
                "reference": "Nexans ref. 10050581",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10050581"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 fils 2,5 C25m",
                "reference": "Nexans ref. 10199400",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "3",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10199400"
                ]
            },
            {
                "title": "Nexans SPEEDFIL 3 FILS 2.5 C25m",
                "reference": "Nexans ref. 10262689",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Transparent",
                    "section": "2.5",
                    "nbcores": "3",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10262689"
                ]
            },
            {
                "title": "Nexans H07V-U 1x2.5 PURPLE C500m",
                "reference": "Nexans ref. 10043653 - Country ref. 01225072",
                "specs": {
                    "packaging": "Coil (500m)",
                    "colorsh": "Violet",
                    "section": "2.5",
                    "nbcores": "1",
                    "length": "500"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10043653"
                ]
            },
            {
                "title": "Nexans H07VU-4-GREEN/YELLOW-C10m",
                "reference": "Nexans ref. 10268895",
                "specs": {
                    "packaging": "Coil (10m)",
                    "colorsh": "Green / Yellow",
                    "section": "4",
                    "nbcores": "1",
                    "length": "10"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10268895"
                ]
            },
            {
                "title": "Nexans H07VU-4-GREEN/YELLOW C25m",
                "reference": "Nexans ref. 10274835",
                "specs": {
                    "packaging": "Coil (25m)",
                    "colorsh": "Green / Yellow",
                    "section": "4",
                    "nbcores": "1",
                    "length": "25"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274835"
                ]
            },
            {
                "title": "Nexans H07VU-4-GREEN/YELLOW C50m",
                "reference": "Nexans ref. 10274836",
                "specs": {
                    "packaging": "Coil (50m)",
                    "colorsh": "Green / Yellow",
                    "section": "4",
                    "nbcores": "1",
                    "length": "50"
                },
                "downloads": [
                    "https://www.nexans.fr/.rest/catalog/v1/product/pdf/10274836"
                ]
            }
        ]
    }]

masterLocal =[
  {
    "id": 1,
    "title": "Amazing Product - Spring Collection",
    "marketName": "Facebook",
    "marketId": 12345,
    "settings": "{\"adType\": \"Carousel\"}",
    "prompt": "Write a product description for a new spring collection",
    "content": "Discover the new season's hottest trends with our Spring Collection! Find stylish clothes, vibrant accessories, and everything you need to refresh your wardrobe. Shop now and enjoy exclusive discounts!",
    "masterProductId": 12344,
    "created_at": "2024-05-14T16:24:00Z"
  },
  {
    "id": 2,
    "title": "Cozy Blankets for Chilly Nights",
    "marketName": "Instagram",
    "marketId": 54321,
    "settings": "{\"postType\": \"Image\"}",
    "prompt": "Create a captivating caption for a photo of a cozy blanket",
    "content": "Snuggle up in pure comfort with our luxurious blankets. Perfect for movie nights, reading by the fireplace, or simply adding a touch of warmth to your home. Available in a variety of colors and styles. Shop now and bring the cozy vibes!",
    "masterProductId": 67890,
    "created_at": "2024-05-14T16:24:00Z"
  },
  {
    "id": 3,
    "title": "Headphones: Immerse Yourself in Sound",
    "marketName": "Google Ads",
    "marketId": 98765,
    "settings": "{\"campaignType\": \"Search\"}",
    "prompt": "Write compelling ad copy for high-quality headphones",
    "content": "Experience unparalleled sound clarity with our premium headphones. Featuring noise cancellation technology, crystal-clear audio, and a comfortable fit, these headphones will elevate your music and entertainment experience. Buy now and lose yourself in the sound!",
    "masterProductId": 12340,
    "created_at": "2024-05-14T16:24:00Z"
  },
  {
    "id": 4,
    "title": "The Ultimate Fitness Tracker",
    "marketName": "Twitter",
    "marketId": 36985,
    "settings": "{\"postType\": \"Video\"}",
    "prompt": "Create a short and engaging video script showcasing a fitness tracker",
    "content": "(Short video showcasing someone using the fitness tracker while running, cycling, and lifting weights) Text overlay: Track your progress, stay motivated, and reach your fitness goals with the ultimate fitness tracker. Shop now and unlock a healthier you!",
    "masterProductId": 12309,
    "created_at": "2024-05-14T16:24:00Z"
  },
  {
    "id": 5,
    "title": "Delicious Recipes for Every Occasion",
    "marketName": "Pinterest",
    "marketId": 74123,
    "settings": "{\"boardName\": \"Healthy Recipes\"}",
    "prompt": "Generate mouthwatering recipe ideas for a Pinterest board",
    "content": "Discover a world of culinary inspiration with our delicious recipes! From quick and easy meals to elaborate feasts, we have something for every taste and occasion. Explore healthy options, indulgent desserts, and everything in between. Start pinning and get ready to cook up a storm!",
    "masterProductId": 123459,
    "created_at": "2024-05-14T16:24:00Z"
  },
]

