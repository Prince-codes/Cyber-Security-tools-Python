<h1 align="center">🔐 Cyber Security Tools in Python 🔐</h1>
<p align="center">
  <b>A curated collection of simple yet powerful cybersecurity scripts for research and educational purposes.</b>
</p>

<hr>

<h2>📂 <b>Contents</b></h2>
<ul>
  <li><a href="#ddospy"><b>ddos.py</b></a> - Simple DDoS Attack Script</li>
  <li><a href="#portscannerpy"><b>port_scanner.py</b></a> - Multithreaded Port Scanner</li>
  <li><a href="#xpy"><b>x.py</b></a> - Batch File Creator</li>
  <li><a href="#x1py"><b>x1.py</b></a> - Mass File Renamer</li>
</ul>

<hr>

<h2 id="ddospy">💥 <b>ddos.py</b></h2>
<ul>
  <li><b>Description:</b> A basic Denial-of-Service (DoS) attack script for <b>educational use only</b>. It sends a large number of requests to the target server/IP.</li>
  <li><b>Features:</b>
    <ul>
      <li>Randomizes user agents and headers to simulate different clients.</li>
      <li>Multi-threaded attack using user-defined number of threads and packets.</li>
      <li>Customizable target IP, port, and packet count.</li>
    </ul>
  </li>
  <li><b>Usage:</b> <i>python ddos.py</i> (You will be prompted for target info.)</li>
  <li><b>⚠️ Note:</b> <i>This script is for educational purposes only. Illegal use is prohibited.</i></li>
</ul>

<hr>

<h2 id="portscannerpy">🔎 <b>port_scanner.py</b></h2>
<ul>
  <li><b>Description:</b> A simple multi-threaded port scanner that checks for open ports in a given range.</li>
  <li><b>Features:</b>
    <ul>
      <li>Resolves domain names to IP addresses.</li>
      <li>Scans user-defined port ranges quickly using threads.</li>
      <li>Identifies and lists open ports.</li>
    </ul>
  </li>
  <li><b>Usage:</b> <i>python port_scanner.py</i> (Input the target and port range when prompted.)</li>
</ul>

<hr>

<h2 id="xpy">📄 <b>x.py</b></h2>
<ul>
  <li><b>Description:</b> Simple script to create multiple files in series, useful for batch file generation (here, C files).</li>
  <li><b>Features:</b>
    <ul>
      <li>Creates files named <b>program_1.c, program_2.c, ...</b> based on user input.</li>
    </ul>
  </li>
  <li><b>Usage:</b> <i>python x.py</i> (Enter the number of files to create.)</li>
</ul>

<hr>

<h2 id="x1py">📝 <b>x1.py</b></h2>
<ul>
  <li><b>Description:</b> Batch renamer script to rename all files in a specified folder with a new base name and sequential numbering.</li>
  <li><b>Features:</b>
    <ul>
      <li>Reads all files in a folder and renames starting from a specified index (default: 26).</li>
      <li>Maintains file extensions and applies a new base name (e.g., program_26.c, program_27.c, ...).</li>
    </ul>
  </li>
  <li><b>Usage:</b> <i>python x1.py</i> (Edit <b>folder_path</b> and <b>base_name</b> as needed in the script.)</li>
</ul>

<hr>

<h2>🚨 <b>Disclaimer</b></h2>
<p>
  <b>This repository is intended for educational and ethical testing purposes only. The author is not responsible for any misuse.</b>
</p>

<p align="center">
  <b>⭐ Star this repo if you find it useful!</b>
</p>
