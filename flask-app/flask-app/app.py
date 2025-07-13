from flask import Flask, render_template_string, jsonify, request
import requests
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    html = """
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Golden Plates | Premium Dining</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --gold-primary: #D4AF37;
            --gold-secondary: #FFD700;
            --gold-tertiary: #F5E7A1;
            --dark-bg: #0F0F0F;
            --light-bg: #1A1A1A;
            --text-light: #F5F5F5;
            --text-gold: #D4AF37;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1c1c1c 100%);
            color: var(--text-light);
            line-height: 1.6;
            overflow-x: hidden;
        }

        .gold-header {
            background: linear-gradient(to right, #1a1a1a, #0f0f0f);
            padding: 1.5rem 2rem;
            border-bottom: 2px solid var(--gold-primary);
            position: relative;
            overflow: hidden;
        }

        .gold-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, transparent, var(--gold-primary), transparent);
        }

        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(to right, var(--gold-primary), var(--gold-secondary));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            letter-spacing: 2px;
            margin-bottom: 0.5rem;
        }

        .tagline {
            text-align: center;
            color: var(--gold-tertiary);
            font-size: 1.1rem;
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 1rem;
        }

        .hero {
            height: 60vh;
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1920&q=80');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 2rem;
            position: relative;
        }

        .hero::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 20px;
            background: linear-gradient(transparent, var(--dark-bg));
        }

        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(to right, var(--gold-primary), var(--gold-secondary));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(212, 175, 55, 0.3);
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin-bottom: 2rem;
            color: var(--text-light);
        }

        .cta-button {
            background: linear-gradient(to right, var(--gold-primary), var(--gold-secondary));
            color: var(--dark-bg);
            border: none;
            padding: 12px 30px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 5px 15px rgba(212, 175, 55, 0.4);
        }

        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(212, 175, 55, 0.6);
        }

        .dishes-intro {
            text-align: center;
            padding: 3rem 2rem;
            max-width: 900px;
            margin: 0 auto;
        }

        .dishes-intro h2 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            color: var(--gold-primary);
        }

        .dishes-intro p {
            font-size: 1.1rem;
            color: var(--text-light);
            margin-bottom: 1rem;
        }

        .protein-highlight {
            display: inline-block;
            background: linear-gradient(to right, rgba(212, 175, 55, 0.2), rgba(255, 215, 0, 0.2));
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-weight: 600;
        }

        .dishes-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
            padding: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .dish-card {
            background: var(--light-bg);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            border: 1px solid rgba(212, 175, 55, 0.3);
        }

        .dish-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(212, 175, 55, 0.2);
            border: 1px solid var(--gold-primary);
        }

        .dish-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--gold-primary), var(--gold-secondary));
        }

        .dish-image {
            height: 200px;
            background-size: cover;
            background-position: center;
        }

        .dish-content {
            padding: 1.5rem;
        }

        .dish-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.6rem;
            margin-bottom: 0.5rem;
            color: var(--gold-primary);
        }

        .dish-description {
            color: #ccc;
            margin-bottom: 1rem;
            min-height: 80px;
        }

        .health-info {
            background: rgba(212, 175, 55, 0.1);
            padding: 1rem;
            border-radius: 8px;
            border-left: 3px solid var(--gold-primary);
        }

        .health-title {
            display: flex;
            align-items: center;
            color: var(--gold-secondary);
            margin-bottom: 0.5rem;
        }

        .health-title i {
            margin-right: 8px;
        }

        .protein-amount {
            color: var(--gold-tertiary);
            font-weight: 600;
            margin-top: 0.5rem;
            display: inline-block;
        }

        .footer {
            background: var(--dark-bg);
            padding: 3rem 2rem;
            text-align: center;
            margin-top: 3rem;
            border-top: 1px solid rgba(212, 175, 55, 0.2);
        }

        .footer-content {
            max-width: 1000px;
            margin: 0 auto;
        }

        .footer-logo {
            font-family: 'Playfair Display', serif;
            font-size: 2rem;
            background: linear-gradient(to right, var(--gold-primary), var(--gold-secondary));
            -webkit-background-clip: text;
            background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
        }

        .contact-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }

        .contact-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--gold-tertiary);
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .social-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background: rgba(212, 175, 55, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--gold-primary);
            transition: all 0.3s ease;
        }

        .social-icon:hover {
            background: var(--gold-primary);
            color: var(--dark-bg);
            transform: translateY(-3px);
        }

        .copyright {
            color: #888;
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        @media (max-width: 768px) {
            .dishes-container {
                grid-template-columns: 1fr;
                padding: 1rem;
            }
            
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .dishes-intro h2 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <header class="gold-header">
        <div class="logo">GOLDEN PLATES</div>
        <div class="tagline">Premium Culinary Experience</div>
    </header>

    <section class="hero">
        <h1>Exquisite Protein-Rich Cuisine</h1>
        <p>Discover our chef's selection of premium dishes crafted with the finest ingredients, each delivering exceptional flavor and nutritional benefits.</p>
        <button class="cta-button">Reserve Your Table</button>
    </section>

    <section class="dishes-intro">
        <h2>Signature Protein Dishes</h2>
        <p>Each of our carefully crafted dishes features high-quality protein sources to nourish your body while delighting your palate. Our chefs combine culinary artistry with nutritional science to create meals that are as beneficial as they are delicious.</p>
        <p>Look for the <span class="protein-highlight">Protein Content</span> information on each dish to understand the nutritional benefits you'll enjoy.</p>
    </section>

    <div class="dishes-container">
        <!-- Dish 1 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Grilled Salmon</h3>
                <p class="dish-description">Atlantic salmon grilled to perfection with lemon-herb butter, served with seasonal vegetables.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-heart"></i> Health Benefits</div>
                    <p>Rich in omega-3 fatty acids that support heart health and reduce inflammation. Excellent source of vitamin D and selenium.</p>
                    <div class="protein-amount">Protein: 34g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 2 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1606755962773-d324e7a7a7d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Herb-Crusted Chicken</h3>
                <p class="dish-description">Free-range chicken breast encrusted with rosemary, thyme, and parmesan, served with quinoa.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-dumbbell"></i> Health Benefits</div>
                    <p>Lean protein source that supports muscle growth and repair. Contains B vitamins essential for energy production.</p>
                    <div class="protein-amount">Protein: 42g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 3 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1626082927389-6cd097cee6a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Filet Mignon</h3>
                <p class="dish-description">Premium beef tenderloin cooked to your preference, served with truffle mashed potatoes.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-bolt"></i> Health Benefits</div>
                    <p>Excellent source of high-quality protein, iron, zinc, and B vitamins. Supports muscle maintenance and immune function.</p>
                    <div class="protein-amount">Protein: 38g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 4 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1594041680534-e8c8cdebd659?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Seared Tuna Steak</h3>
                <p class="dish-description">Sushi-grade tuna lightly seared with sesame crust, served with ginger-soy glaze.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-brain"></i> Health Benefits</div>
                    <p>Rich in omega-3s and selenium, supporting brain health and cognitive function. Excellent lean protein source.</p>
                    <div class="protein-amount">Protein: 40g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 5 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1555939594-58d7cb561ad1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Lamb Chops</h3>
                <p class="dish-description">New Zealand lamb chops with mint pesto, served with roasted root vegetables.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-leaf"></i> Health Benefits</div>
                    <p>High in protein, iron, and zinc. Contains conjugated linoleic acid (CLA) which may have antioxidant properties.</p>
                    <div class="protein-amount">Protein: 36g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 6 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1606491956689-2ea866880c84?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Shrimp Scampi</h3>
                <p class="dish-description">Jumbo shrimp sautéed in garlic, white wine, and lemon butter sauce over linguine.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-shield-alt"></i> Health Benefits</div>
                    <p>Low in calories but high in protein and selenium. Contains astaxanthin, a powerful antioxidant for skin health.</p>
                    <div class="protein-amount">Protein: 32g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 7 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1626082927389-6cd097cee6a6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Venison Medallions</h3>
                <p class="dish-description">Lean venison medallions with juniper berry sauce and wild mushroom risotto.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-fire"></i> Health Benefits</div>
                    <p>Extremely lean protein source, rich in B vitamins and iron. Lower in fat and calories than beef.</p>
                    <div class="protein-amount">Protein: 41g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 8 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1562967916-eb82221dfb92?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Duck Confit</h3>
                <p class="dish-description">Slow-cooked duck leg with crispy skin, served with cherry reduction and parsnip puree.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-apple-alt"></i> Health Benefits</div>
                    <p>Rich in iron and selenium. Contains monounsaturated fats similar to olive oil. Good source of B vitamins.</p>
                    <div class="protein-amount">Protein: 35g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 9 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1625944525533-473f1d7a2183?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Scallops with Lentils</h3>
                <p class="dish-description">Pan-seared sea scallops on a bed of French lentils with lemon-herb vinaigrette.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-heartbeat"></i> Health Benefits</div>
                    <p>Low in calories but high in protein and minerals. Scallops are a good source of magnesium and potassium.</p>
                    <div class="protein-amount">Protein: 33g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 10 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1550304943-4f24f54ddde9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Beef Short Rib</h3>
                <p class="dish-description">Braised beef short ribs with red wine reduction, served with celery root puree.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-bone"></i> Health Benefits</div>
                    <p>Excellent source of collagen and gelatin which support joint health. Rich in iron and zinc.</p>
                    <div class="protein-amount">Protein: 39g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 11 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1606755962773-d324e7a7a7d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Turkey Roulade</h3>
                <p class="dish-description">Herb-stuffed turkey breast rolled and roasted, served with cranberry compote.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-feather"></i> Health Benefits</div>
                    <p>Lean protein source that's rich in selenium, B vitamins, and tryptophan. Supports immune function.</p>
                    <div class="protein-amount">Protein: 37g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 12 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Pork Tenderloin</h3>
                <p class="dish-description">Rosemary-garlic pork tenderloin with apple cider glaze and sweet potato mash.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-seedling"></i> Health Benefits</div>
                    <p>Excellent source of thiamine, selenium, and B vitamins. Contains important minerals like zinc and phosphorus.</p>
                    <div class="protein-amount">Protein: 36g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 13 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1606755962773-d324e7a7a7d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Halibut with Quinoa</h3>
                <p class="dish-description">Pan-seared halibut with lemon-caper sauce served on a bed of tri-color quinoa.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-water"></i> Health Benefits</div>
                    <p>Rich in omega-3s and high-quality protein. Contains magnesium, potassium, and vitamin B6.</p>
                    <div class="protein-amount">Protein: 35g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 14 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Bison Burger</h3>
                <p class="dish-description">Grass-fed bison burger with caramelized onions and garlic aioli on brioche bun.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-wind"></i> Health Benefits</div>
                    <p>Leaner than beef with higher protein content. Rich in iron, zinc, and omega-3 fatty acids.</p>
                    <div class="protein-amount">Protein: 40g per serving</div>
                </div>
            </div>
        </div>

        <!-- Dish 15 -->
        <div class="dish-card">
            <div class="dish-image" style="background-image: url('https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80');"></div>
            <div class="dish-content">
                <h3 class="dish-title">Lobster Tail</h3>
                <p class="dish-description">Butter-poached lobster tail with drawn butter and lemon, served with asparagus.</p>
                <div class="health-info">
                    <div class="health-title"><i class="fas fa-star"></i> Health Benefits</div>
                    <p>Excellent source of lean protein, selenium, and vitamin B12. Contains copper and zinc for immune support.</p>
                    <div class="protein-amount">Protein: 31g per serving</div>
                </div>
            </div>
        </div>
    </div>

    <footer class="footer">
        <div class="footer-content">
            <div class="footer-logo">GOLDEN PLATES</div>
            <p>Where culinary excellence meets nutritional perfection</p>
            
            <div class="contact-info">
                <div class="contact-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <span>123 Gourmet Avenue, Culinary District</span>
                </div>
                <div class="contact-item">
                    <i class="fas fa-phone"></i>
                    <span>(555) 123-4567</span>
                </div>
                <div class="contact-item">
                    <i class="fas fa-envelope"></i>
                    <span>reservations@goldenplates.com</span>
                </div>
            </div>
            
            <div class="social-links">
                <a href="#" class="social-icon"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-instagram"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-twitter"></i></a>
                <a href="#" class="social-icon"><i class="fab fa-tripadvisor"></i></a>
            </div>
            
            <div class="copyright">
                &copy; 2023 Golden Plates Restaurant. All rights reserved.
            </div>
        </div>
    </footer>
</body>
</html>
    """
    return render_template_string(html)

@app.route('/fetch')
def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()[:5]
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to fetch data"}), 500

@app.route('/health')
def health():
    return jsonify({"status": "App is healthy and running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
