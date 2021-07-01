<img src="https://www.tabbykatz.com/hbnb.png">
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="AirBnB_clone_0"></a>AirBnB_clone</h1>
<h1 class="code-line" data-line-start=1 data-line-end=2 ><a id="Synopsis_1"></a>Synopsis</h1>
<p class="has-line-data" data-line-start="3" data-line-end="5">The Airbnb clone project for which we are creating a copy of the <a href="https://www.airbnb.com/">Airbnb</a>.<br>
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…</p>
<h2 class="code-line" data-line-start=7 data-line-end=8 ><a id="Features_7"></a>Features</h2>
<h3 class="code-line" data-line-start=9 data-line-end=10 ><a id="Command_Interpreter_9"></a>Command Interpreter</h3>
<h4 class="code-line" data-line-start=11 data-line-end=12 ><a id="Description_11"></a>Description</h4>
<p class="has-line-data" data-line-start="12" data-line-end="13">The Command Interpreter is used to manage the whole application’s functionality from the command line.</p>
<h4 class="code-line" data-line-start=14 data-line-end=15 ><a id="Functionalities_of_this_command_interpreter_14"></a>Functionalities of this command interpreter</h4>
<ul>
<li class="has-line-data" data-line-start="15" data-line-end="16">Crete a new object.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Retrieve an object from a file, database, etc.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">Execute operation on objects. e.g. Count, compute statistics, etc.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">Update object’s attributes.</li>
<li class="has-line-data" data-line-start="19" data-line-end="21">Destroy an object.</li>
</ul>
<h4 class="code-line" data-line-start=21 data-line-end=22 ><a id="Usage_21"></a>Usage</h4>
<p class="has-line-data" data-line-start="23" data-line-end="24">To launch the console application in interactive mode simply run:</p>
<pre><code class="has-line-data" data-line-start="26" data-line-end="28" class="language-bash">$ ./console.py
</code></pre>
<pre><code class="has-line-data" data-line-start="30" data-line-end="60" class="language-bash">(hbnb)<span class="hljs-built_in">help</span>

Documented commands (<span class="hljs-built_in">type</span> <span class="hljs-built_in">help</span> &lt;topic&gt;):


(hbnb)<span class="hljs-built_in">help</span> all

Prints all string representation of
all instances based or not on the class name

(hbnb)<span class="hljs-built_in">help</span> create

Creates an instance of a defined class.

(hbnb)destroy
** class name missing **

(hbnb)create BaseModel
<span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa

(hbnb)show BaseModel <span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa
[BaseModel] (<span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa) {<span class="hljs-string">'id'</span>: <span class="hljs-string">'17fa8a0a-f3f8-453f-b0d6-d636802fcafa'</span>, <span class="hljs-string">'created_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971047</span>), <span class="hljs-string">'updated_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971310</span>)}


update BaseModel <span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa first_name <span class="hljs-string">"Juan Carabali"</span>
(hbnb)

(hbnb)show BaseModel <span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa
[BaseModel] (<span class="hljs-number">17</span>fa8a0a<span class="hljs-operator">-f</span>3f8-<span class="hljs-number">453</span>f-b0d6<span class="hljs-operator">-d</span>636802fcafa) {<span class="hljs-string">'id'</span>: <span class="hljs-string">'17fa8a0a-f3f8-453f-b0d6-d636802fcafa'</span>, <span class="hljs-string">'created_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971047</span>), <span class="hljs-string">'updated_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971310</span>), <span class="hljs-string">'first_name'</span>: <span class="hljs-string">'Juan Carabali'</span>}
</code></pre>
<p class="has-line-data" data-line-start="61" data-line-end="62">or to use the non-interactive mode run:</p>
<pre><code class="has-line-data" data-line-start="64" data-line-end="66" class="language-bash"><span class="hljs-built_in">echo</span> <span class="hljs-string">"your-command-goes-here"</span> | ./console.py
</code></pre>
<pre><code class="has-line-data" data-line-start="68" data-line-end="86" class="language-bash"><span class="hljs-built_in">echo</span> <span class="hljs-string">"help"</span> | ./console.py

Documented commands (<span class="hljs-built_in">type</span> <span class="hljs-built_in">help</span> &lt;topic&gt;):
========================================
EOF  all  create  destroy  <span class="hljs-built_in">help</span>  quit  show  update

<span class="hljs-built_in">echo</span> <span class="hljs-string">"help quit"</span> | ./console.py
(hbnb)Quit <span class="hljs-built_in">command</span> to <span class="hljs-built_in">exit</span> the program

<span class="hljs-built_in">echo</span> <span class="hljs-string">"create BaseModel"</span> | ./console.py
(hbnb)acacc732-<span class="hljs-number">5</span>d67-<span class="hljs-number">4</span>d94-bc1a-b32b43dcabb6

<span class="hljs-built_in">echo</span> <span class="hljs-string">"show BaseModel acacc732-5d67-4d94-bc1a-b32b43dcabb6"</span> | ./console.py
(hbnb)[BaseModel] (acacc732-<span class="hljs-number">5</span>d67-<span class="hljs-number">4</span>d94-bc1a-b32b43dcabb6) {<span class="hljs-string">'id'</span>: <span class="hljs-string">'acacc732-5d67-4d94-bc1a-b32b43dcabb6'</span>, <span class="hljs-string">'created_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">45</span>, <span class="hljs-number">966638</span>), <span class="hljs-string">'updated_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">3</span>, <span class="hljs-number">5</span>, <span class="hljs-number">45</span>, <span class="hljs-number">967401</span>)}

<span class="hljs-built_in">echo</span> <span class="hljs-string">"show BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9"</span> | ./console.py
(hbnb)[BaseModel] (<span class="hljs-number">17</span>e3e759-<span class="hljs-number">2</span>f88-<span class="hljs-number">4555</span>-<span class="hljs-number">825</span>c<span class="hljs-operator">-d</span>2a1866772f9) {<span class="hljs-string">'id'</span>: <span class="hljs-string">'17e3e759-2f88-4555-825c-d2a1866772f9'</span>, <span class="hljs-string">'created_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971047</span>), <span class="hljs-string">'updated_at'</span>: datetime.datetime(<span class="hljs-number">2021</span>, <span class="hljs-number">7</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">48</span>, <span class="hljs-number">30</span>, <span class="hljs-number">971310</span>), <span class="hljs-string">'first_name'</span>: <span class="hljs-string">'Juan Carabali'</span>}
</code></pre>
<h4 class="code-line" data-line-start=88 data-line-end=89 ><a id="Commands_88"></a>Commands</h4>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Commands</th>
<th>Description</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>help</strong> or <strong>?</strong></td>
<td>Displays the documented commands.</td>
<td><strong>help</strong></td>
</tr>
<tr>
<td><strong>quit</strong></td>
<td>Exits the program.</td>
<td><strong>quit</strong></td>
</tr>
<tr>
<td><strong>EOF</strong></td>
<td>Ends the program. Used when files are passed into the program.</td>
<td>N/A</td>
</tr>
<tr>
<td><strong>create</strong></td>
<td>Creates a new instance of the &lt;class_name&gt;. Creates a Json file with the object representation. and prints the id of created object.</td>
<td><strong>create</strong> &lt;class_name&gt;</td>
</tr>
<tr>
<td><strong>show</strong></td>
<td>Prints the string representation of an instance based on the class name and id.</td>
<td><strong>show</strong> &lt;class_name class_id&gt;</td>
</tr>
<tr>
<td><strong>destroy</strong></td>
<td>Deletes and instance base on the class name and id.</td>
<td><strong>destroy</strong> &lt;class_name class_id&gt;</td>
</tr>
<tr>
<td><strong>all</strong></td>
<td>Prints all string representation of all instances based or not on the class name</td>
<td><strong>all</strong> or <strong>all</strong> &lt;class_name class_id&gt;</td>
</tr>
<tr>
<td><strong>update</strong></td>
<td>Updates an instance based on the class name and id by adding or updating attribute</td>
<td><strong>update</strong> &lt;class_name class_id key value&gt;</td>
</tr>
</tbody>
</table>
<h2 class="code-line" data-line-start=101 data-line-end=102 ><a id="Tests_101"></a>Tests</h2>
<p class="has-line-data" data-line-start="103" data-line-end="105">If you wish to run at the test for this application all of the test are located<br>
under the <strong>test/</strong> folder and can execute all of them by simply running:</p>
<pre><code class="has-line-data" data-line-start="107" data-line-end="109" class="language-bash">python3 -m unittest discover tests
</code></pre>
<p class="has-line-data" data-line-start="110" data-line-end="111">from the root directory.</p>
<h2 class="code-line" data-line-start=113 data-line-end=114 ><a id="Bugs_113"></a>Bugs</h2>
<ul>
<li class="has-line-data" data-line-start="115" data-line-end="116">No known bugs at this time.</li>
</ul>
