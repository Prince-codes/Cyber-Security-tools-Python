<h1 align="center">🔐 Cyber Security Tools in Python 🔐</h1>
<p align="center">
  <b>A collection of simple cybersecurity scripts for research and educational purposes. Use responsibly.</b>
</p>

<hr>

<h2>📂 <b>Contents</b></h2>
<ul>
  <li><a href="#ddospy"><b>ddos.py</b></a> - Denial of Service (DoS) Attack Script</li>
  <li><a href="#portscannerpy"><b>port_scanner.py</b></a> - Multi-threaded Port Scanner</li>
  <li><a href="#webstresstestingpy"><b>web-stress-testing.py</b></a> - Web Server Stress Test</li>
  <li><a href="#createmultifilespy"><b>create_multiple-files.py</b></a> - Batch File Creator</li>
  <li><a href="#renamemultifilespy"><b>rename_multiple-files.py</b></a> - Batch File Renamer</li>
</ul>

<hr>

<h2 id="ddospy">💥 <b>ddos.py</b></h2>
<ul>
  <li><b>Description:</b> A basic Denial-of-Service (DoS) attack script for <b>educational use only</b>. Sends a large number of packets to a target IP and port.</li>
  <li><b>Features:</b>
    <ul>
      <li>Randomizes user agents and headers.</li>
      <li>Multi-threaded attack with user-defined threads and packets.</li>
      <li>Customizable target IP, port, and packet count.</li>
    </ul>
  </li>
  <li><b>Usage:</b> <code>python ddos.py</code> (You will be prompted for target info.)</li>
  <li><b>⚠️ Note:</b> <i>For educational purposes only. Illegal use is prohibited.</i></li>
</ul>

<hr>

<h2 id="portscannerpy">🔎 <b>port_scanner.py</b></h2>
<ul>
  <li><b>Description:</b> A simple multi-threaded port scanner that checks for open ports in a given range.</li>
  <li><b>Features:</b>
    <ul>
      <li>Resolves domain names to IP addresses.</li>
      <li>Scans user-defined port ranges using threads.</li>
      <li>Identifies and lists open ports.</li>
    </ul>
  </li>
  <li><b>Usage:</b> <code>python port_scanner.py</code> (Input the target and port range when prompted.)</li>
</ul>

<hr>

<h2 id="webstresstestingpy">🌐 <b>web-stress-testing.py</b></h2>
<ul>
  <li><b>Description:</b> Demonstrates multi-threaded TCP connection attempts to a target IP and port. Each thread repeatedly sends a simple HTTP GET request. Useful for learning about threading and sockets in Python, or for stress testing a web server.</li>
  <li><b>Usage:</b> <code>python web-stress-testing.py</code> (You will be prompted for target IP, port, and number of threads.)</li>
  <li><b>Features:</b>
    <ul>
      <li>Prompts user for target IP, port, and thread count.</li>
      <li>Spawns multiple threads, each making repeated TCP connections and sending HTTP requests.</li>
      <li>Handles connection errors gracefully.</li>
    </ul>
  </li>
</ul>

<hr>

<h2 id="createmultifilespy">📄 <b>create_multiple-files.py</b></h2>
<ul>
  <li><b>Description:</b> Script to create multiple files at once. Useful for batch file generation or testing.</li>
  <li><b>Usage:</b> <code>python create_multiple-files.py</code></li>
</ul>

<hr>

<h2 id="renamemultifilespy">📝 <b>rename_multiple-files.py</b></h2>
<ul>
  <li><b>Description:</b> Batch renamer script to rename all files in a specified folder with a new base name and sequential numbering.</li>
  <li><b>Usage:</b> <code>python rename_multiple-files.py</code></li>
</ul>

<h2>🚨 <b>Disclaimer</b></h2>
<p>
  <b>This repository is intended for educational and ethical testing purposes only. The author is not responsible for any misuse.</b>
</p>

<p align="center">
  <b>⭐ Star this repo if you find it useful!</b>
</p>

---

<h3 align="center" style="color: gray;">
💧 Created with ❤️ by <b>Prince Raj Singh</b> from <b style="font-family: 'Courier New', monospace; letter-spacing: 2px;">ＣＡＲＮＡＧＥ ＳＥＮＴＩＮＥＬＳ</b> 💧
</h3>