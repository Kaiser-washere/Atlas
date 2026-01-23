#!/bin/bash

echo "🔧 Starting Atlas Setup..."

# Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install requests dnspython python-whois colorama

# Compile C++ scanner
echo "⚙️ Compiling C++ port scanner..."
if [ -f "native/scanner.cpp" ]; then
    g++ -O2 -std=c++17 native/scanner.cpp -o native/scanner
    echo "✅ Scanner compiled: native/scanner"
else
    echo "❌ scanner.cpp not found!"
fi

# Prepare Ruby scraper
echo "💎 Preparing Ruby scraper..."
if [ -f "native/scraper.rb" ]; then
    chmod +x native/scraper.rb
    echo "✅ Scraper ready: native/scraper.rb"
else
    echo "❌ scraper.rb not found!"
fi

# Done
echo "🎉 Atlas setup completed!"
echo "🚀 Example usage:"
echo "   python3 core.py -t example.com -m whois"
echo "   python3 core.py -t example.com -m dns"
echo "   python3 core.py -t 8.8.8.8 -m geoip"
echo "   python3 core.py -t www.google.com -m http"
echo "   python3 core.py -t example.com -m scanner --ports 22,80,443"
echo "   python3 core.py -t mars -m social"
