<h1>🌐 Atlas - Info Gathering Tool</h1>


<p>
Atlas is a hybrid prototype tool 🔧 for information gathering. It combines <b>Python</b>, <b>C++</b>, and <b>Ruby</b> modules into a single CLI.  
Designed for security researchers 🕵️, penetration testers 💻, and developers 👨‍💻 who want a modular and colorful way to collect domain, IP, and social footprint data.
</p>

<h2> Features</h2>
<ul>
  <li>🔍 <b>WHOIS</b> – Retrieve domain registration details.</li>
  <li>🌐 <b>DNS</b> – Query A, MX, TXT, NS, and CNAME records.</li>
  <li>📍 <b>GeoIP</b> – Get IP geolocation and ASN information.</li>
  <li>📡 <b>HTTP</b> – Fetch HTTP headers and status codes.</li>
  <li>⚡ <b>Scanner (C++)</b> – Fast port scanning using native C++.</li>
  <li>👤 <b>Social (Ruby)</b> – Check username availability across platforms.</li>
</ul>

<h2>⚙️ Installation</h2>
<p>
Atlas ships with an <code>install.sh</code> script for quick setup.  
Simply run:
</p>

<pre>
chmod +x install.sh
./install.sh
</pre>

<p>
This will install Python dependencies, compile the C++ scanner, and prepare the Ruby scraper automatically ✅.
</p>

<h2> Usage</h2>
<pre>
python3 core.py -t example.com -m whois
python3 core.py -t example.com -m dns
python3 core.py -t 8.8.8.8 -m geoip
python3 core.py -t www.google.com -m http
python3 core.py -t example.com -m scanner --ports 22,80,443
python3 core.py -t username -m social
</pre>

<h2>🎨 Output Colors</h2>
<ul>
  <li>🟢 Green – Success (e.g., open ports, status 200)</li>
  <li>🔴 Red – Errors or not found (e.g., status 403/404)</li>
  <li>🟡 Yellow – Warnings or redirects (e.g., status 301)</li>
  <li>🟣 Magenta – Server errors (e.g., status 500)</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
Atlas/
 ├── core.py          # Main CLI entrypoint
 ├── modules/         # Python modules (whois, dns, geoip, http, scanner, social)
 ├── native/          # C++ scanner + Ruby scraper
 ├── utils/           # Colors + ASCII banner
 └── install.sh       # Quick setup script
</pre>

<h2>📌 Status</h2>
<p>
This is a prototype release 🧪. Future improvements may include JSON/CSV export 📑, additional social platforms 🌐, and extended scanning capabilities 🔦.
</p>
<h1>educational use only</h1>
