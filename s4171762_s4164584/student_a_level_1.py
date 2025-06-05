def get_page_html(form_data):
    first = lambda key: form_data.get(key, [""])[0]
    airport = first("airport")
    arrival_time = first("arrival_time")
    page_html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <title>SkySafe – Level 1</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f0f0f0;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 1000px;
                margin: auto;
                background: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }}
            header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
            }}
            header h1 {{ margin: 0; }}
            header h1 span {{
                font-size: .6em;
                color: gray;
            }}
            nav a {{ margin-right: 12px; }}
            form {{ margin: 20px 0; }}
            input[type=text] {{
                margin: 10px 5px;
                padding: 8px;
                width: 280px;
            }}
            button {{
                padding: 8px 14px;
                margin: 10px 5px;
                cursor: pointer;
            }}
            .columns {{
                display: flex;
                flex-wrap: wrap;
                gap: 40px;
                margin-top: 20px;
            }}
            .box {{
                flex: 1 1 420px;
                background: #f9f9f9;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #ddd;
            }}
            ul {{ list-style: none; padding: 0; }}
        </style>
    </head>
    <body>
        <div class='container'>
            <header>
                <h1>SkySafe <span>weatherreport.com</span></h1>
                <nav>
                    <a href='/'>Page 1A</a>
                    <a href='/page2a'>Page 2A</a>
                    <a href='/page3a'>Page 3A</a>
                </nav>
            </header>
            <form method='get'>
                <input type='text' name='airport' placeholder='Please type in your destination airport' value='{airport}'>
                <input type='text' name='arrival_time' placeholder='Please type in your expected arrival time' value='{arrival_time}'>
                <button type='submit'>Submit</button>
            </form>
            <div class='columns'>
                <section class='box'>
                    <h2>METAR / TAF Summary</h2>
                    <ul>
                        <li><strong>Airport:</strong> {airport or '—'}</li>
                        <li><strong>Arrival Time:</strong> {arrival_time or '—'}</li>
                        <li><strong>Conditions:</strong> Clear</li>
                        <li><strong>Temperature:</strong> 20 °C</li>
                        <li><strong>Visibility:</strong> 10 km</li>
                        <li><strong>Headwind:</strong> 5 knots</li>
                        <li><strong>Cloud ceiling:</strong> 2000 ft</li>
                        <li><strong>Overcast:</strong> No</li>
                    </ul>
                </section>
                <section class='box'>
                    <h2>7-Day Forecast</h2>
                    <h3>Weather Warnings</h3>
                    <p>None</p>
                    <h3>Weather Type</h3>
                    <p>Sunny</p>
                    <h3>Visibility</h3>
                    <p>Good throughout the week</p>
                </section>
            </div>
        </div>
    </body>
    </html>
    """
    return page_html
