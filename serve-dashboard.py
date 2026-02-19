#!/usr/bin/env python3
"""
Simple HTTP server to serve the progress dashboard
Usage: python3 serve-dashboard.py [port]
Default port: 8080
"""
import http.server
import socketserver
import sys
import webbrowser
import os
from pathlib import Path

def main():
    # Default port
    port = 8080
    
    # Parse command line argument for port
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            sys.exit(1)
    
    # Change to script directory to serve files from here
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Create HTTP server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🚀 Progress Dashboard Server starting...")
            print(f"📊 Dashboard URL: http://localhost:{port}/progress-dashboard.html")
            print(f"🌐 Server running on port {port}")
            print(f"📁 Serving files from: {script_dir}")
            print(f"⏹️  Press Ctrl+C to stop")
            print()
            
            # Try to open in browser
            try:
                dashboard_url = f"http://localhost:{port}/progress-dashboard.html"
                print(f"🌍 Opening dashboard in browser: {dashboard_url}")
                webbrowser.open(dashboard_url)
            except Exception as e:
                print(f"⚠️  Could not auto-open browser: {e}")
                print(f"💡 Manual URL: http://localhost:{port}/progress-dashboard.html")
            
            httpd.serve_forever()
            
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {port} is already in use")
            print(f"💡 Try a different port: python3 serve-dashboard.py {port + 1}")
        else:
            print(f"❌ Server error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n⏹️  Dashboard server stopped")

if __name__ == "__main__":
    main()