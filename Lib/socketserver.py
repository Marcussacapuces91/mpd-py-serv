<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: ee8d999b6e05 Lib/socketserver.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="http://hg.python.org/">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/ee8d999b6e05">log</a></li>
<li><a href="/cpython/graph/ee8d999b6e05">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/branches">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/ee8d999b6e05">changeset</a></li>
<li><a href="/cpython/file/ee8d999b6e05/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/socketserver.py">latest</a></li>
<li><a href="/cpython/diff/ee8d999b6e05/Lib/socketserver.py">diff</a></li>
<li><a href="/cpython/comparison/ee8d999b6e05/Lib/socketserver.py">comparison</a></li>
<li><a href="/cpython/annotate/ee8d999b6e05/Lib/socketserver.py">annotate</a></li>
<li><a href="/cpython/log/ee8d999b6e05/Lib/socketserver.py">file log</a></li>
<li><a href="/cpython/raw-file/ee8d999b6e05/Lib/socketserver.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2><a href="/cpython/">cpython</a></h2>
<h3>view Lib/socketserver.py @ 81129:ee8d999b6e05</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">find changesets by author, revision,
files, or words in the commit message</div>
</form>

<div class="description">Forward port new test for SSLSocket.connect_ex()</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#65;&#110;&#116;&#111;&#105;&#110;&#101;&#32;&#80;&#105;&#116;&#114;&#111;&#117;&#32;&#60;&#115;&#111;&#108;&#105;&#112;&#115;&#105;&#115;&#64;&#112;&#105;&#116;&#114;&#111;&#117;&#46;&#110;&#101;&#116;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Fri, 28 Dec 2012 19:07:43 +0100</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/f8e7fcd581ff/Lib/socketserver.py">f8e7fcd581ff</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"><a href="/cpython/file/7734c3020a47/Lib/socketserver.py">7734c3020a47</a> </td>
</tr>

</table>

<div class="overflow">
<div class="sourcefirst"> line source</div>

<div class="parity0 source"><a href="#l1" id="l1">     1</a> <span class="sd">&quot;&quot;&quot;Generic socket server classes.</span></div>
<div class="parity1 source"><a href="#l2" id="l2">     2</a> </div>
<div class="parity0 source"><a href="#l3" id="l3">     3</a> <span class="sd">This module tries to capture the various aspects of defining a server:</span></div>
<div class="parity1 source"><a href="#l4" id="l4">     4</a> </div>
<div class="parity0 source"><a href="#l5" id="l5">     5</a> <span class="sd">For socket-based servers:</span></div>
<div class="parity1 source"><a href="#l6" id="l6">     6</a> </div>
<div class="parity0 source"><a href="#l7" id="l7">     7</a> <span class="sd">- address family:</span></div>
<div class="parity1 source"><a href="#l8" id="l8">     8</a> <span class="sd">        - AF_INET{,6}: IP (Internet Protocol) sockets (default)</span></div>
<div class="parity0 source"><a href="#l9" id="l9">     9</a> <span class="sd">        - AF_UNIX: Unix domain sockets</span></div>
<div class="parity1 source"><a href="#l10" id="l10">    10</a> <span class="sd">        - others, e.g. AF_DECNET are conceivable (see &lt;socket.h&gt;</span></div>
<div class="parity0 source"><a href="#l11" id="l11">    11</a> <span class="sd">- socket type:</span></div>
<div class="parity1 source"><a href="#l12" id="l12">    12</a> <span class="sd">        - SOCK_STREAM (reliable stream, e.g. TCP)</span></div>
<div class="parity0 source"><a href="#l13" id="l13">    13</a> <span class="sd">        - SOCK_DGRAM (datagrams, e.g. UDP)</span></div>
<div class="parity1 source"><a href="#l14" id="l14">    14</a> </div>
<div class="parity0 source"><a href="#l15" id="l15">    15</a> <span class="sd">For request-based servers (including socket-based):</span></div>
<div class="parity1 source"><a href="#l16" id="l16">    16</a> </div>
<div class="parity0 source"><a href="#l17" id="l17">    17</a> <span class="sd">- client address verification before further looking at the request</span></div>
<div class="parity1 source"><a href="#l18" id="l18">    18</a> <span class="sd">        (This is actually a hook for any processing that needs to look</span></div>
<div class="parity0 source"><a href="#l19" id="l19">    19</a> <span class="sd">         at the request before anything else, e.g. logging)</span></div>
<div class="parity1 source"><a href="#l20" id="l20">    20</a> <span class="sd">- how to handle multiple requests:</span></div>
<div class="parity0 source"><a href="#l21" id="l21">    21</a> <span class="sd">        - synchronous (one request is handled at a time)</span></div>
<div class="parity1 source"><a href="#l22" id="l22">    22</a> <span class="sd">        - forking (each request is handled by a new process)</span></div>
<div class="parity0 source"><a href="#l23" id="l23">    23</a> <span class="sd">        - threading (each request is handled by a new thread)</span></div>
<div class="parity1 source"><a href="#l24" id="l24">    24</a> </div>
<div class="parity0 source"><a href="#l25" id="l25">    25</a> <span class="sd">The classes in this module favor the server type that is simplest to</span></div>
<div class="parity1 source"><a href="#l26" id="l26">    26</a> <span class="sd">write: a synchronous TCP/IP server.  This is bad class design, but</span></div>
<div class="parity0 source"><a href="#l27" id="l27">    27</a> <span class="sd">save some typing.  (There&#39;s also the issue that a deep class hierarchy</span></div>
<div class="parity1 source"><a href="#l28" id="l28">    28</a> <span class="sd">slows down method lookups.)</span></div>
<div class="parity0 source"><a href="#l29" id="l29">    29</a> </div>
<div class="parity1 source"><a href="#l30" id="l30">    30</a> <span class="sd">There are five classes in an inheritance diagram, four of which represent</span></div>
<div class="parity0 source"><a href="#l31" id="l31">    31</a> <span class="sd">synchronous servers of four types:</span></div>
<div class="parity1 source"><a href="#l32" id="l32">    32</a> </div>
<div class="parity0 source"><a href="#l33" id="l33">    33</a> <span class="sd">        +------------+</span></div>
<div class="parity1 source"><a href="#l34" id="l34">    34</a> <span class="sd">        | BaseServer |</span></div>
<div class="parity0 source"><a href="#l35" id="l35">    35</a> <span class="sd">        +------------+</span></div>
<div class="parity1 source"><a href="#l36" id="l36">    36</a> <span class="sd">              |</span></div>
<div class="parity0 source"><a href="#l37" id="l37">    37</a> <span class="sd">              v</span></div>
<div class="parity1 source"><a href="#l38" id="l38">    38</a> <span class="sd">        +-----------+        +------------------+</span></div>
<div class="parity0 source"><a href="#l39" id="l39">    39</a> <span class="sd">        | TCPServer |-------&gt;| UnixStreamServer |</span></div>
<div class="parity1 source"><a href="#l40" id="l40">    40</a> <span class="sd">        +-----------+        +------------------+</span></div>
<div class="parity0 source"><a href="#l41" id="l41">    41</a> <span class="sd">              |</span></div>
<div class="parity1 source"><a href="#l42" id="l42">    42</a> <span class="sd">              v</span></div>
<div class="parity0 source"><a href="#l43" id="l43">    43</a> <span class="sd">        +-----------+        +--------------------+</span></div>
<div class="parity1 source"><a href="#l44" id="l44">    44</a> <span class="sd">        | UDPServer |-------&gt;| UnixDatagramServer |</span></div>
<div class="parity0 source"><a href="#l45" id="l45">    45</a> <span class="sd">        +-----------+        +--------------------+</span></div>
<div class="parity1 source"><a href="#l46" id="l46">    46</a> </div>
<div class="parity0 source"><a href="#l47" id="l47">    47</a> <span class="sd">Note that UnixDatagramServer derives from UDPServer, not from</span></div>
<div class="parity1 source"><a href="#l48" id="l48">    48</a> <span class="sd">UnixStreamServer -- the only difference between an IP and a Unix</span></div>
<div class="parity0 source"><a href="#l49" id="l49">    49</a> <span class="sd">stream server is the address family, which is simply repeated in both</span></div>
<div class="parity1 source"><a href="#l50" id="l50">    50</a> <span class="sd">unix server classes.</span></div>
<div class="parity0 source"><a href="#l51" id="l51">    51</a> </div>
<div class="parity1 source"><a href="#l52" id="l52">    52</a> <span class="sd">Forking and threading versions of each type of server can be created</span></div>
<div class="parity0 source"><a href="#l53" id="l53">    53</a> <span class="sd">using the ForkingMixIn and ThreadingMixIn mix-in classes.  For</span></div>
<div class="parity1 source"><a href="#l54" id="l54">    54</a> <span class="sd">instance, a threading UDP server class is created as follows:</span></div>
<div class="parity0 source"><a href="#l55" id="l55">    55</a> </div>
<div class="parity1 source"><a href="#l56" id="l56">    56</a> <span class="sd">        class ThreadingUDPServer(ThreadingMixIn, UDPServer): pass</span></div>
<div class="parity0 source"><a href="#l57" id="l57">    57</a> </div>
<div class="parity1 source"><a href="#l58" id="l58">    58</a> <span class="sd">The Mix-in class must come first, since it overrides a method defined</span></div>
<div class="parity0 source"><a href="#l59" id="l59">    59</a> <span class="sd">in UDPServer! Setting the various member variables also changes</span></div>
<div class="parity1 source"><a href="#l60" id="l60">    60</a> <span class="sd">the behavior of the underlying server mechanism.</span></div>
<div class="parity0 source"><a href="#l61" id="l61">    61</a> </div>
<div class="parity1 source"><a href="#l62" id="l62">    62</a> <span class="sd">To implement a service, you must derive a class from</span></div>
<div class="parity0 source"><a href="#l63" id="l63">    63</a> <span class="sd">BaseRequestHandler and redefine its handle() method.  You can then run</span></div>
<div class="parity1 source"><a href="#l64" id="l64">    64</a> <span class="sd">various versions of the service by combining one of the server classes</span></div>
<div class="parity0 source"><a href="#l65" id="l65">    65</a> <span class="sd">with your request handler class.</span></div>
<div class="parity1 source"><a href="#l66" id="l66">    66</a> </div>
<div class="parity0 source"><a href="#l67" id="l67">    67</a> <span class="sd">The request handler class must be different for datagram or stream</span></div>
<div class="parity1 source"><a href="#l68" id="l68">    68</a> <span class="sd">services.  This can be hidden by using the request handler</span></div>
<div class="parity0 source"><a href="#l69" id="l69">    69</a> <span class="sd">subclasses StreamRequestHandler or DatagramRequestHandler.</span></div>
<div class="parity1 source"><a href="#l70" id="l70">    70</a> </div>
<div class="parity0 source"><a href="#l71" id="l71">    71</a> <span class="sd">Of course, you still have to use your head!</span></div>
<div class="parity1 source"><a href="#l72" id="l72">    72</a> </div>
<div class="parity0 source"><a href="#l73" id="l73">    73</a> <span class="sd">For instance, it makes no sense to use a forking server if the service</span></div>
<div class="parity1 source"><a href="#l74" id="l74">    74</a> <span class="sd">contains state in memory that can be modified by requests (since the</span></div>
<div class="parity0 source"><a href="#l75" id="l75">    75</a> <span class="sd">modifications in the child process would never reach the initial state</span></div>
<div class="parity1 source"><a href="#l76" id="l76">    76</a> <span class="sd">kept in the parent process and passed to each child).  In this case,</span></div>
<div class="parity0 source"><a href="#l77" id="l77">    77</a> <span class="sd">you can use a threading server, but you will probably have to use</span></div>
<div class="parity1 source"><a href="#l78" id="l78">    78</a> <span class="sd">locks to avoid two requests that come in nearly simultaneous to apply</span></div>
<div class="parity0 source"><a href="#l79" id="l79">    79</a> <span class="sd">conflicting changes to the server state.</span></div>
<div class="parity1 source"><a href="#l80" id="l80">    80</a> </div>
<div class="parity0 source"><a href="#l81" id="l81">    81</a> <span class="sd">On the other hand, if you are building e.g. an HTTP server, where all</span></div>
<div class="parity1 source"><a href="#l82" id="l82">    82</a> <span class="sd">data is stored externally (e.g. in the file system), a synchronous</span></div>
<div class="parity0 source"><a href="#l83" id="l83">    83</a> <span class="sd">class will essentially render the service &quot;deaf&quot; while one request is</span></div>
<div class="parity1 source"><a href="#l84" id="l84">    84</a> <span class="sd">being handled -- which may be for a very long time if a client is slow</span></div>
<div class="parity0 source"><a href="#l85" id="l85">    85</a> <span class="sd">to read all the data it has requested.  Here a threading or forking</span></div>
<div class="parity1 source"><a href="#l86" id="l86">    86</a> <span class="sd">server is appropriate.</span></div>
<div class="parity0 source"><a href="#l87" id="l87">    87</a> </div>
<div class="parity1 source"><a href="#l88" id="l88">    88</a> <span class="sd">In some cases, it may be appropriate to process part of a request</span></div>
<div class="parity0 source"><a href="#l89" id="l89">    89</a> <span class="sd">synchronously, but to finish processing in a forked child depending on</span></div>
<div class="parity1 source"><a href="#l90" id="l90">    90</a> <span class="sd">the request data.  This can be implemented by using a synchronous</span></div>
<div class="parity0 source"><a href="#l91" id="l91">    91</a> <span class="sd">server and doing an explicit fork in the request handler class</span></div>
<div class="parity1 source"><a href="#l92" id="l92">    92</a> <span class="sd">handle() method.</span></div>
<div class="parity0 source"><a href="#l93" id="l93">    93</a> </div>
<div class="parity1 source"><a href="#l94" id="l94">    94</a> <span class="sd">Another approach to handling multiple simultaneous requests in an</span></div>
<div class="parity0 source"><a href="#l95" id="l95">    95</a> <span class="sd">environment that supports neither threads nor fork (or where these are</span></div>
<div class="parity1 source"><a href="#l96" id="l96">    96</a> <span class="sd">too expensive or inappropriate for the service) is to maintain an</span></div>
<div class="parity0 source"><a href="#l97" id="l97">    97</a> <span class="sd">explicit table of partially finished requests and to use select() to</span></div>
<div class="parity1 source"><a href="#l98" id="l98">    98</a> <span class="sd">decide which request to work on next (or whether to handle a new</span></div>
<div class="parity0 source"><a href="#l99" id="l99">    99</a> <span class="sd">incoming request).  This is particularly important for stream services</span></div>
<div class="parity1 source"><a href="#l100" id="l100">   100</a> <span class="sd">where each client can potentially be connected for a long time (if</span></div>
<div class="parity0 source"><a href="#l101" id="l101">   101</a> <span class="sd">threads or subprocesses cannot be used).</span></div>
<div class="parity1 source"><a href="#l102" id="l102">   102</a> </div>
<div class="parity0 source"><a href="#l103" id="l103">   103</a> <span class="sd">Future work:</span></div>
<div class="parity1 source"><a href="#l104" id="l104">   104</a> <span class="sd">- Standard classes for Sun RPC (which uses either UDP or TCP)</span></div>
<div class="parity0 source"><a href="#l105" id="l105">   105</a> <span class="sd">- Standard mix-in classes to implement various authentication</span></div>
<div class="parity1 source"><a href="#l106" id="l106">   106</a> <span class="sd">  and encryption schemes</span></div>
<div class="parity0 source"><a href="#l107" id="l107">   107</a> <span class="sd">- Standard framework for select-based multiplexing</span></div>
<div class="parity1 source"><a href="#l108" id="l108">   108</a> </div>
<div class="parity0 source"><a href="#l109" id="l109">   109</a> <span class="sd">XXX Open problems:</span></div>
<div class="parity1 source"><a href="#l110" id="l110">   110</a> <span class="sd">- What to do with out-of-band data?</span></div>
<div class="parity0 source"><a href="#l111" id="l111">   111</a> </div>
<div class="parity1 source"><a href="#l112" id="l112">   112</a> <span class="sd">BaseServer:</span></div>
<div class="parity0 source"><a href="#l113" id="l113">   113</a> <span class="sd">- split generic &quot;request&quot; functionality out into BaseServer class.</span></div>
<div class="parity1 source"><a href="#l114" id="l114">   114</a> <span class="sd">  Copyright (C) 2000  Luke Kenneth Casson Leighton &lt;lkcl@samba.org&gt;</span></div>
<div class="parity0 source"><a href="#l115" id="l115">   115</a> </div>
<div class="parity1 source"><a href="#l116" id="l116">   116</a> <span class="sd">  example: read entries from a SQL database (requires overriding</span></div>
<div class="parity0 source"><a href="#l117" id="l117">   117</a> <span class="sd">  get_request() to return a table entry from the database).</span></div>
<div class="parity1 source"><a href="#l118" id="l118">   118</a> <span class="sd">  entry is processed by a RequestHandlerClass.</span></div>
<div class="parity0 source"><a href="#l119" id="l119">   119</a> </div>
<div class="parity1 source"><a href="#l120" id="l120">   120</a> <span class="sd">&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l121" id="l121">   121</a> </div>
<div class="parity1 source"><a href="#l122" id="l122">   122</a> <span class="c"># Author of the BaseServer patch: Luke Kenneth Casson Leighton</span></div>
<div class="parity0 source"><a href="#l123" id="l123">   123</a> </div>
<div class="parity1 source"><a href="#l124" id="l124">   124</a> <span class="c"># XXX Warning!</span></div>
<div class="parity0 source"><a href="#l125" id="l125">   125</a> <span class="c"># There is a test suite for this module, but it cannot be run by the</span></div>
<div class="parity1 source"><a href="#l126" id="l126">   126</a> <span class="c"># standard regression test.</span></div>
<div class="parity0 source"><a href="#l127" id="l127">   127</a> <span class="c"># To run it manually, run Lib/test/test_socketserver.py.</span></div>
<div class="parity1 source"><a href="#l128" id="l128">   128</a> </div>
<div class="parity0 source"><a href="#l129" id="l129">   129</a> <span class="n">__version__</span> <span class="o">=</span> <span class="s">&quot;0.4&quot;</span></div>
<div class="parity1 source"><a href="#l130" id="l130">   130</a> </div>
<div class="parity0 source"><a href="#l131" id="l131">   131</a> </div>
<div class="parity1 source"><a href="#l132" id="l132">   132</a> <span class="kn">import</span> <span class="nn">socket</span></div>
<div class="parity0 source"><a href="#l133" id="l133">   133</a> <span class="kn">import</span> <span class="nn">select</span></div>
<div class="parity1 source"><a href="#l134" id="l134">   134</a> <span class="kn">import</span> <span class="nn">sys</span></div>
<div class="parity0 source"><a href="#l135" id="l135">   135</a> <span class="kn">import</span> <span class="nn">os</span></div>
<div class="parity1 source"><a href="#l136" id="l136">   136</a> <span class="kn">import</span> <span class="nn">errno</span></div>
<div class="parity0 source"><a href="#l137" id="l137">   137</a> <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l138" id="l138">   138</a>     <span class="kn">import</span> <span class="nn">threading</span></div>
<div class="parity0 source"><a href="#l139" id="l139">   139</a> <span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l140" id="l140">   140</a>     <span class="kn">import</span> <span class="nn">dummy_threading</span> <span class="kn">as</span> <span class="nn">threading</span></div>
<div class="parity0 source"><a href="#l141" id="l141">   141</a> </div>
<div class="parity1 source"><a href="#l142" id="l142">   142</a> <span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;TCPServer&quot;</span><span class="p">,</span><span class="s">&quot;UDPServer&quot;</span><span class="p">,</span><span class="s">&quot;ForkingUDPServer&quot;</span><span class="p">,</span><span class="s">&quot;ForkingTCPServer&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l143" id="l143">   143</a>            <span class="s">&quot;ThreadingUDPServer&quot;</span><span class="p">,</span><span class="s">&quot;ThreadingTCPServer&quot;</span><span class="p">,</span><span class="s">&quot;BaseRequestHandler&quot;</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l144" id="l144">   144</a>            <span class="s">&quot;StreamRequestHandler&quot;</span><span class="p">,</span><span class="s">&quot;DatagramRequestHandler&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l145" id="l145">   145</a>            <span class="s">&quot;ThreadingMixIn&quot;</span><span class="p">,</span> <span class="s">&quot;ForkingMixIn&quot;</span><span class="p">]</span></div>
<div class="parity1 source"><a href="#l146" id="l146">   146</a> <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">socket</span><span class="p">,</span> <span class="s">&quot;AF_UNIX&quot;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l147" id="l147">   147</a>     <span class="n">__all__</span><span class="o">.</span><span class="n">extend</span><span class="p">([</span><span class="s">&quot;UnixStreamServer&quot;</span><span class="p">,</span><span class="s">&quot;UnixDatagramServer&quot;</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l148" id="l148">   148</a>                     <span class="s">&quot;ThreadingUnixStreamServer&quot;</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l149" id="l149">   149</a>                     <span class="s">&quot;ThreadingUnixDatagramServer&quot;</span><span class="p">])</span></div>
<div class="parity1 source"><a href="#l150" id="l150">   150</a> </div>
<div class="parity0 source"><a href="#l151" id="l151">   151</a> <span class="k">def</span> <span class="nf">_eintr_retry</span><span class="p">(</span><span class="n">func</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l152" id="l152">   152</a>     <span class="sd">&quot;&quot;&quot;restart a system call interrupted by EINTR&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l153" id="l153">   153</a>     <span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l154" id="l154">   154</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l155" id="l155">   155</a>             <span class="k">return</span> <span class="n">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l156" id="l156">   156</a>         <span class="k">except</span> <span class="p">(</span><span class="ne">OSError</span><span class="p">,</span> <span class="n">select</span><span class="o">.</span><span class="n">error</span><span class="p">)</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l157" id="l157">   157</a>             <span class="k">if</span> <span class="n">e</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">!=</span> <span class="n">errno</span><span class="o">.</span><span class="n">EINTR</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l158" id="l158">   158</a>                 <span class="k">raise</span></div>
<div class="parity0 source"><a href="#l159" id="l159">   159</a> </div>
<div class="parity1 source"><a href="#l160" id="l160">   160</a> <span class="k">class</span> <span class="nc">BaseServer</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l161" id="l161">   161</a> </div>
<div class="parity1 source"><a href="#l162" id="l162">   162</a>     <span class="sd">&quot;&quot;&quot;Base class for server classes.</span></div>
<div class="parity0 source"><a href="#l163" id="l163">   163</a> </div>
<div class="parity1 source"><a href="#l164" id="l164">   164</a> <span class="sd">    Methods for the caller:</span></div>
<div class="parity0 source"><a href="#l165" id="l165">   165</a> </div>
<div class="parity1 source"><a href="#l166" id="l166">   166</a> <span class="sd">    - __init__(server_address, RequestHandlerClass)</span></div>
<div class="parity0 source"><a href="#l167" id="l167">   167</a> <span class="sd">    - serve_forever(poll_interval=0.5)</span></div>
<div class="parity1 source"><a href="#l168" id="l168">   168</a> <span class="sd">    - shutdown()</span></div>
<div class="parity0 source"><a href="#l169" id="l169">   169</a> <span class="sd">    - handle_request()  # if you do not use serve_forever()</span></div>
<div class="parity1 source"><a href="#l170" id="l170">   170</a> <span class="sd">    - fileno() -&gt; int   # for select()</span></div>
<div class="parity0 source"><a href="#l171" id="l171">   171</a> </div>
<div class="parity1 source"><a href="#l172" id="l172">   172</a> <span class="sd">    Methods that may be overridden:</span></div>
<div class="parity0 source"><a href="#l173" id="l173">   173</a> </div>
<div class="parity1 source"><a href="#l174" id="l174">   174</a> <span class="sd">    - server_bind()</span></div>
<div class="parity0 source"><a href="#l175" id="l175">   175</a> <span class="sd">    - server_activate()</span></div>
<div class="parity1 source"><a href="#l176" id="l176">   176</a> <span class="sd">    - get_request() -&gt; request, client_address</span></div>
<div class="parity0 source"><a href="#l177" id="l177">   177</a> <span class="sd">    - handle_timeout()</span></div>
<div class="parity1 source"><a href="#l178" id="l178">   178</a> <span class="sd">    - verify_request(request, client_address)</span></div>
<div class="parity0 source"><a href="#l179" id="l179">   179</a> <span class="sd">    - server_close()</span></div>
<div class="parity1 source"><a href="#l180" id="l180">   180</a> <span class="sd">    - process_request(request, client_address)</span></div>
<div class="parity0 source"><a href="#l181" id="l181">   181</a> <span class="sd">    - shutdown_request(request)</span></div>
<div class="parity1 source"><a href="#l182" id="l182">   182</a> <span class="sd">    - close_request(request)</span></div>
<div class="parity0 source"><a href="#l183" id="l183">   183</a> <span class="sd">    - handle_error()</span></div>
<div class="parity1 source"><a href="#l184" id="l184">   184</a> </div>
<div class="parity0 source"><a href="#l185" id="l185">   185</a> <span class="sd">    Methods for derived classes:</span></div>
<div class="parity1 source"><a href="#l186" id="l186">   186</a> </div>
<div class="parity0 source"><a href="#l187" id="l187">   187</a> <span class="sd">    - finish_request(request, client_address)</span></div>
<div class="parity1 source"><a href="#l188" id="l188">   188</a> </div>
<div class="parity0 source"><a href="#l189" id="l189">   189</a> <span class="sd">    Class variables that may be overridden by derived classes or</span></div>
<div class="parity1 source"><a href="#l190" id="l190">   190</a> <span class="sd">    instances:</span></div>
<div class="parity0 source"><a href="#l191" id="l191">   191</a> </div>
<div class="parity1 source"><a href="#l192" id="l192">   192</a> <span class="sd">    - timeout</span></div>
<div class="parity0 source"><a href="#l193" id="l193">   193</a> <span class="sd">    - address_family</span></div>
<div class="parity1 source"><a href="#l194" id="l194">   194</a> <span class="sd">    - socket_type</span></div>
<div class="parity0 source"><a href="#l195" id="l195">   195</a> <span class="sd">    - allow_reuse_address</span></div>
<div class="parity1 source"><a href="#l196" id="l196">   196</a> </div>
<div class="parity0 source"><a href="#l197" id="l197">   197</a> <span class="sd">    Instance variables:</span></div>
<div class="parity1 source"><a href="#l198" id="l198">   198</a> </div>
<div class="parity0 source"><a href="#l199" id="l199">   199</a> <span class="sd">    - RequestHandlerClass</span></div>
<div class="parity1 source"><a href="#l200" id="l200">   200</a> <span class="sd">    - socket</span></div>
<div class="parity0 source"><a href="#l201" id="l201">   201</a> </div>
<div class="parity1 source"><a href="#l202" id="l202">   202</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l203" id="l203">   203</a> </div>
<div class="parity1 source"><a href="#l204" id="l204">   204</a>     <span class="n">timeout</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l205" id="l205">   205</a> </div>
<div class="parity1 source"><a href="#l206" id="l206">   206</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_address</span><span class="p">,</span> <span class="n">RequestHandlerClass</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l207" id="l207">   207</a>         <span class="sd">&quot;&quot;&quot;Constructor.  May be extended, do not override.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l208" id="l208">   208</a>         <span class="bp">self</span><span class="o">.</span><span class="n">server_address</span> <span class="o">=</span> <span class="n">server_address</span></div>
<div class="parity0 source"><a href="#l209" id="l209">   209</a>         <span class="bp">self</span><span class="o">.</span><span class="n">RequestHandlerClass</span> <span class="o">=</span> <span class="n">RequestHandlerClass</span></div>
<div class="parity1 source"><a href="#l210" id="l210">   210</a>         <span class="bp">self</span><span class="o">.</span><span class="n">__is_shut_down</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Event</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l211" id="l211">   211</a>         <span class="bp">self</span><span class="o">.</span><span class="n">__shutdown_request</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity1 source"><a href="#l212" id="l212">   212</a> </div>
<div class="parity0 source"><a href="#l213" id="l213">   213</a>     <span class="k">def</span> <span class="nf">server_activate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l214" id="l214">   214</a>         <span class="sd">&quot;&quot;&quot;Called by constructor to activate the server.</span></div>
<div class="parity0 source"><a href="#l215" id="l215">   215</a> </div>
<div class="parity1 source"><a href="#l216" id="l216">   216</a> <span class="sd">        May be overridden.</span></div>
<div class="parity0 source"><a href="#l217" id="l217">   217</a> </div>
<div class="parity1 source"><a href="#l218" id="l218">   218</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l219" id="l219">   219</a>         <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l220" id="l220">   220</a> </div>
<div class="parity0 source"><a href="#l221" id="l221">   221</a>     <span class="k">def</span> <span class="nf">serve_forever</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">poll_interval</span><span class="o">=</span><span class="mf">0.5</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l222" id="l222">   222</a>         <span class="sd">&quot;&quot;&quot;Handle one request at a time until shutdown.</span></div>
<div class="parity0 source"><a href="#l223" id="l223">   223</a> </div>
<div class="parity1 source"><a href="#l224" id="l224">   224</a> <span class="sd">        Polls for shutdown every poll_interval seconds. Ignores</span></div>
<div class="parity0 source"><a href="#l225" id="l225">   225</a> <span class="sd">        self.timeout. If you need to do periodic tasks, do them in</span></div>
<div class="parity1 source"><a href="#l226" id="l226">   226</a> <span class="sd">        another thread.</span></div>
<div class="parity0 source"><a href="#l227" id="l227">   227</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l228" id="l228">   228</a>         <span class="bp">self</span><span class="o">.</span><span class="n">__is_shut_down</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l229" id="l229">   229</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l230" id="l230">   230</a>             <span class="k">while</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">__shutdown_request</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l231" id="l231">   231</a>                 <span class="c"># XXX: Consider using another file descriptor or</span></div>
<div class="parity1 source"><a href="#l232" id="l232">   232</a>                 <span class="c"># connecting to the socket to wake this up instead of</span></div>
<div class="parity0 source"><a href="#l233" id="l233">   233</a>                 <span class="c"># polling. Polling reduces our responsiveness to a</span></div>
<div class="parity1 source"><a href="#l234" id="l234">   234</a>                 <span class="c"># shutdown request and wastes cpu at all other times.</span></div>
<div class="parity0 source"><a href="#l235" id="l235">   235</a>                 <span class="n">r</span><span class="p">,</span> <span class="n">w</span><span class="p">,</span> <span class="n">e</span> <span class="o">=</span> <span class="n">_eintr_retry</span><span class="p">(</span><span class="n">select</span><span class="o">.</span><span class="n">select</span><span class="p">,</span> <span class="p">[</span><span class="bp">self</span><span class="p">],</span> <span class="p">[],</span> <span class="p">[],</span></div>
<div class="parity1 source"><a href="#l236" id="l236">   236</a>                                        <span class="n">poll_interval</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l237" id="l237">   237</a>                 <span class="k">if</span> <span class="bp">self</span> <span class="ow">in</span> <span class="n">r</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l238" id="l238">   238</a>                     <span class="bp">self</span><span class="o">.</span><span class="n">_handle_request_noblock</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l239" id="l239">   239</a>         <span class="k">finally</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l240" id="l240">   240</a>             <span class="bp">self</span><span class="o">.</span><span class="n">__shutdown_request</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity0 source"><a href="#l241" id="l241">   241</a>             <span class="bp">self</span><span class="o">.</span><span class="n">__is_shut_down</span><span class="o">.</span><span class="n">set</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l242" id="l242">   242</a> </div>
<div class="parity0 source"><a href="#l243" id="l243">   243</a>     <span class="k">def</span> <span class="nf">shutdown</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l244" id="l244">   244</a>         <span class="sd">&quot;&quot;&quot;Stops the serve_forever loop.</span></div>
<div class="parity0 source"><a href="#l245" id="l245">   245</a> </div>
<div class="parity1 source"><a href="#l246" id="l246">   246</a> <span class="sd">        Blocks until the loop has finished. This must be called while</span></div>
<div class="parity0 source"><a href="#l247" id="l247">   247</a> <span class="sd">        serve_forever() is running in another thread, or it will</span></div>
<div class="parity1 source"><a href="#l248" id="l248">   248</a> <span class="sd">        deadlock.</span></div>
<div class="parity0 source"><a href="#l249" id="l249">   249</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l250" id="l250">   250</a>         <span class="bp">self</span><span class="o">.</span><span class="n">__shutdown_request</span> <span class="o">=</span> <span class="bp">True</span></div>
<div class="parity0 source"><a href="#l251" id="l251">   251</a>         <span class="bp">self</span><span class="o">.</span><span class="n">__is_shut_down</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l252" id="l252">   252</a> </div>
<div class="parity0 source"><a href="#l253" id="l253">   253</a>     <span class="c"># The distinction between handling, getting, processing and</span></div>
<div class="parity1 source"><a href="#l254" id="l254">   254</a>     <span class="c"># finishing a request is fairly arbitrary.  Remember:</span></div>
<div class="parity0 source"><a href="#l255" id="l255">   255</a>     <span class="c">#</span></div>
<div class="parity1 source"><a href="#l256" id="l256">   256</a>     <span class="c"># - handle_request() is the top-level call.  It calls</span></div>
<div class="parity0 source"><a href="#l257" id="l257">   257</a>     <span class="c">#   select, get_request(), verify_request() and process_request()</span></div>
<div class="parity1 source"><a href="#l258" id="l258">   258</a>     <span class="c"># - get_request() is different for stream or datagram sockets</span></div>
<div class="parity0 source"><a href="#l259" id="l259">   259</a>     <span class="c"># - process_request() is the place that may fork a new process</span></div>
<div class="parity1 source"><a href="#l260" id="l260">   260</a>     <span class="c">#   or create a new thread to finish the request</span></div>
<div class="parity0 source"><a href="#l261" id="l261">   261</a>     <span class="c"># - finish_request() instantiates the request handler class;</span></div>
<div class="parity1 source"><a href="#l262" id="l262">   262</a>     <span class="c">#   this constructor will handle the request all by itself</span></div>
<div class="parity0 source"><a href="#l263" id="l263">   263</a> </div>
<div class="parity1 source"><a href="#l264" id="l264">   264</a>     <span class="k">def</span> <span class="nf">handle_request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l265" id="l265">   265</a>         <span class="sd">&quot;&quot;&quot;Handle one request, possibly blocking.</span></div>
<div class="parity1 source"><a href="#l266" id="l266">   266</a> </div>
<div class="parity0 source"><a href="#l267" id="l267">   267</a> <span class="sd">        Respects self.timeout.</span></div>
<div class="parity1 source"><a href="#l268" id="l268">   268</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l269" id="l269">   269</a>         <span class="c"># Support people who used socket.settimeout() to escape</span></div>
<div class="parity1 source"><a href="#l270" id="l270">   270</a>         <span class="c"># handle_request before self.timeout was available.</span></div>
<div class="parity0 source"><a href="#l271" id="l271">   271</a>         <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">gettimeout</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l272" id="l272">   272</a>         <span class="k">if</span> <span class="n">timeout</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l273" id="l273">   273</a>             <span class="n">timeout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span></div>
<div class="parity1 source"><a href="#l274" id="l274">   274</a>         <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l275" id="l275">   275</a>             <span class="n">timeout</span> <span class="o">=</span> <span class="nb">min</span><span class="p">(</span><span class="n">timeout</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l276" id="l276">   276</a>         <span class="n">fd_sets</span> <span class="o">=</span> <span class="n">_eintr_retry</span><span class="p">(</span><span class="n">select</span><span class="o">.</span><span class="n">select</span><span class="p">,</span> <span class="p">[</span><span class="bp">self</span><span class="p">],</span> <span class="p">[],</span> <span class="p">[],</span> <span class="n">timeout</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l277" id="l277">   277</a>         <span class="k">if</span> <span class="ow">not</span> <span class="n">fd_sets</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span></div>
<div class="parity1 source"><a href="#l278" id="l278">   278</a>             <span class="bp">self</span><span class="o">.</span><span class="n">handle_timeout</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l279" id="l279">   279</a>             <span class="k">return</span></div>
<div class="parity1 source"><a href="#l280" id="l280">   280</a>         <span class="bp">self</span><span class="o">.</span><span class="n">_handle_request_noblock</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l281" id="l281">   281</a> </div>
<div class="parity1 source"><a href="#l282" id="l282">   282</a>     <span class="k">def</span> <span class="nf">_handle_request_noblock</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l283" id="l283">   283</a>         <span class="sd">&quot;&quot;&quot;Handle one request, without blocking.</span></div>
<div class="parity1 source"><a href="#l284" id="l284">   284</a> </div>
<div class="parity0 source"><a href="#l285" id="l285">   285</a> <span class="sd">        I assume that select.select has returned that the socket is</span></div>
<div class="parity1 source"><a href="#l286" id="l286">   286</a> <span class="sd">        readable before this function was called, so there should be</span></div>
<div class="parity0 source"><a href="#l287" id="l287">   287</a> <span class="sd">        no risk of blocking in get_request().</span></div>
<div class="parity1 source"><a href="#l288" id="l288">   288</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l289" id="l289">   289</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l290" id="l290">   290</a>             <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_request</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l291" id="l291">   291</a>         <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l292" id="l292">   292</a>             <span class="k">return</span></div>
<div class="parity0 source"><a href="#l293" id="l293">   293</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">verify_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l294" id="l294">   294</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l295" id="l295">   295</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">process_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l296" id="l296">   296</a>             <span class="k">except</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l297" id="l297">   297</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">handle_error</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l298" id="l298">   298</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l299" id="l299">   299</a> </div>
<div class="parity1 source"><a href="#l300" id="l300">   300</a>     <span class="k">def</span> <span class="nf">handle_timeout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l301" id="l301">   301</a>         <span class="sd">&quot;&quot;&quot;Called if no new request arrives within self.timeout.</span></div>
<div class="parity1 source"><a href="#l302" id="l302">   302</a> </div>
<div class="parity0 source"><a href="#l303" id="l303">   303</a> <span class="sd">        Overridden by ForkingMixIn.</span></div>
<div class="parity1 source"><a href="#l304" id="l304">   304</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l305" id="l305">   305</a>         <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l306" id="l306">   306</a> </div>
<div class="parity0 source"><a href="#l307" id="l307">   307</a>     <span class="k">def</span> <span class="nf">verify_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l308" id="l308">   308</a>         <span class="sd">&quot;&quot;&quot;Verify the request.  May be overridden.</span></div>
<div class="parity0 source"><a href="#l309" id="l309">   309</a> </div>
<div class="parity1 source"><a href="#l310" id="l310">   310</a> <span class="sd">        Return True if we should proceed with this request.</span></div>
<div class="parity0 source"><a href="#l311" id="l311">   311</a> </div>
<div class="parity1 source"><a href="#l312" id="l312">   312</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l313" id="l313">   313</a>         <span class="k">return</span> <span class="bp">True</span></div>
<div class="parity1 source"><a href="#l314" id="l314">   314</a> </div>
<div class="parity0 source"><a href="#l315" id="l315">   315</a>     <span class="k">def</span> <span class="nf">process_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l316" id="l316">   316</a>         <span class="sd">&quot;&quot;&quot;Call finish_request.</span></div>
<div class="parity0 source"><a href="#l317" id="l317">   317</a> </div>
<div class="parity1 source"><a href="#l318" id="l318">   318</a> <span class="sd">        Overridden by ForkingMixIn and ThreadingMixIn.</span></div>
<div class="parity0 source"><a href="#l319" id="l319">   319</a> </div>
<div class="parity1 source"><a href="#l320" id="l320">   320</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l321" id="l321">   321</a>         <span class="bp">self</span><span class="o">.</span><span class="n">finish_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l322" id="l322">   322</a>         <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l323" id="l323">   323</a> </div>
<div class="parity1 source"><a href="#l324" id="l324">   324</a>     <span class="k">def</span> <span class="nf">server_close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l325" id="l325">   325</a>         <span class="sd">&quot;&quot;&quot;Called to clean-up the server.</span></div>
<div class="parity1 source"><a href="#l326" id="l326">   326</a> </div>
<div class="parity0 source"><a href="#l327" id="l327">   327</a> <span class="sd">        May be overridden.</span></div>
<div class="parity1 source"><a href="#l328" id="l328">   328</a> </div>
<div class="parity0 source"><a href="#l329" id="l329">   329</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l330" id="l330">   330</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l331" id="l331">   331</a> </div>
<div class="parity1 source"><a href="#l332" id="l332">   332</a>     <span class="k">def</span> <span class="nf">finish_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l333" id="l333">   333</a>         <span class="sd">&quot;&quot;&quot;Finish one request by instantiating RequestHandlerClass.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l334" id="l334">   334</a>         <span class="bp">self</span><span class="o">.</span><span class="n">RequestHandlerClass</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l335" id="l335">   335</a> </div>
<div class="parity1 source"><a href="#l336" id="l336">   336</a>     <span class="k">def</span> <span class="nf">shutdown_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l337" id="l337">   337</a>         <span class="sd">&quot;&quot;&quot;Called to shutdown and close an individual request.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l338" id="l338">   338</a>         <span class="bp">self</span><span class="o">.</span><span class="n">close_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l339" id="l339">   339</a> </div>
<div class="parity1 source"><a href="#l340" id="l340">   340</a>     <span class="k">def</span> <span class="nf">close_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l341" id="l341">   341</a>         <span class="sd">&quot;&quot;&quot;Called to clean up an individual request.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l342" id="l342">   342</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l343" id="l343">   343</a> </div>
<div class="parity1 source"><a href="#l344" id="l344">   344</a>     <span class="k">def</span> <span class="nf">handle_error</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l345" id="l345">   345</a>         <span class="sd">&quot;&quot;&quot;Handle an error gracefully.  May be overridden.</span></div>
<div class="parity1 source"><a href="#l346" id="l346">   346</a> </div>
<div class="parity0 source"><a href="#l347" id="l347">   347</a> <span class="sd">        The default is to print a traceback and continue.</span></div>
<div class="parity1 source"><a href="#l348" id="l348">   348</a> </div>
<div class="parity0 source"><a href="#l349" id="l349">   349</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l350" id="l350">   350</a>         <span class="k">print</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="o">*</span><span class="mi">40</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l351" id="l351">   351</a>         <span class="k">print</span><span class="p">(</span><span class="s">&#39;Exception happened during processing of request from&#39;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s">&#39; &#39;</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l352" id="l352">   352</a>         <span class="k">print</span><span class="p">(</span><span class="n">client_address</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l353" id="l353">   353</a>         <span class="kn">import</span> <span class="nn">traceback</span></div>
<div class="parity1 source"><a href="#l354" id="l354">   354</a>         <span class="n">traceback</span><span class="o">.</span><span class="n">print_exc</span><span class="p">()</span> <span class="c"># XXX But this goes to stderr!</span></div>
<div class="parity0 source"><a href="#l355" id="l355">   355</a>         <span class="k">print</span><span class="p">(</span><span class="s">&#39;-&#39;</span><span class="o">*</span><span class="mi">40</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l356" id="l356">   356</a> </div>
<div class="parity0 source"><a href="#l357" id="l357">   357</a> </div>
<div class="parity1 source"><a href="#l358" id="l358">   358</a> <span class="k">class</span> <span class="nc">TCPServer</span><span class="p">(</span><span class="n">BaseServer</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l359" id="l359">   359</a> </div>
<div class="parity1 source"><a href="#l360" id="l360">   360</a>     <span class="sd">&quot;&quot;&quot;Base class for various socket-based server classes.</span></div>
<div class="parity0 source"><a href="#l361" id="l361">   361</a> </div>
<div class="parity1 source"><a href="#l362" id="l362">   362</a> <span class="sd">    Defaults to synchronous IP stream (i.e., TCP).</span></div>
<div class="parity0 source"><a href="#l363" id="l363">   363</a> </div>
<div class="parity1 source"><a href="#l364" id="l364">   364</a> <span class="sd">    Methods for the caller:</span></div>
<div class="parity0 source"><a href="#l365" id="l365">   365</a> </div>
<div class="parity1 source"><a href="#l366" id="l366">   366</a> <span class="sd">    - __init__(server_address, RequestHandlerClass, bind_and_activate=True)</span></div>
<div class="parity0 source"><a href="#l367" id="l367">   367</a> <span class="sd">    - serve_forever(poll_interval=0.5)</span></div>
<div class="parity1 source"><a href="#l368" id="l368">   368</a> <span class="sd">    - shutdown()</span></div>
<div class="parity0 source"><a href="#l369" id="l369">   369</a> <span class="sd">    - handle_request()  # if you don&#39;t use serve_forever()</span></div>
<div class="parity1 source"><a href="#l370" id="l370">   370</a> <span class="sd">    - fileno() -&gt; int   # for select()</span></div>
<div class="parity0 source"><a href="#l371" id="l371">   371</a> </div>
<div class="parity1 source"><a href="#l372" id="l372">   372</a> <span class="sd">    Methods that may be overridden:</span></div>
<div class="parity0 source"><a href="#l373" id="l373">   373</a> </div>
<div class="parity1 source"><a href="#l374" id="l374">   374</a> <span class="sd">    - server_bind()</span></div>
<div class="parity0 source"><a href="#l375" id="l375">   375</a> <span class="sd">    - server_activate()</span></div>
<div class="parity1 source"><a href="#l376" id="l376">   376</a> <span class="sd">    - get_request() -&gt; request, client_address</span></div>
<div class="parity0 source"><a href="#l377" id="l377">   377</a> <span class="sd">    - handle_timeout()</span></div>
<div class="parity1 source"><a href="#l378" id="l378">   378</a> <span class="sd">    - verify_request(request, client_address)</span></div>
<div class="parity0 source"><a href="#l379" id="l379">   379</a> <span class="sd">    - process_request(request, client_address)</span></div>
<div class="parity1 source"><a href="#l380" id="l380">   380</a> <span class="sd">    - shutdown_request(request)</span></div>
<div class="parity0 source"><a href="#l381" id="l381">   381</a> <span class="sd">    - close_request(request)</span></div>
<div class="parity1 source"><a href="#l382" id="l382">   382</a> <span class="sd">    - handle_error()</span></div>
<div class="parity0 source"><a href="#l383" id="l383">   383</a> </div>
<div class="parity1 source"><a href="#l384" id="l384">   384</a> <span class="sd">    Methods for derived classes:</span></div>
<div class="parity0 source"><a href="#l385" id="l385">   385</a> </div>
<div class="parity1 source"><a href="#l386" id="l386">   386</a> <span class="sd">    - finish_request(request, client_address)</span></div>
<div class="parity0 source"><a href="#l387" id="l387">   387</a> </div>
<div class="parity1 source"><a href="#l388" id="l388">   388</a> <span class="sd">    Class variables that may be overridden by derived classes or</span></div>
<div class="parity0 source"><a href="#l389" id="l389">   389</a> <span class="sd">    instances:</span></div>
<div class="parity1 source"><a href="#l390" id="l390">   390</a> </div>
<div class="parity0 source"><a href="#l391" id="l391">   391</a> <span class="sd">    - timeout</span></div>
<div class="parity1 source"><a href="#l392" id="l392">   392</a> <span class="sd">    - address_family</span></div>
<div class="parity0 source"><a href="#l393" id="l393">   393</a> <span class="sd">    - socket_type</span></div>
<div class="parity1 source"><a href="#l394" id="l394">   394</a> <span class="sd">    - request_queue_size (only for stream sockets)</span></div>
<div class="parity0 source"><a href="#l395" id="l395">   395</a> <span class="sd">    - allow_reuse_address</span></div>
<div class="parity1 source"><a href="#l396" id="l396">   396</a> </div>
<div class="parity0 source"><a href="#l397" id="l397">   397</a> <span class="sd">    Instance variables:</span></div>
<div class="parity1 source"><a href="#l398" id="l398">   398</a> </div>
<div class="parity0 source"><a href="#l399" id="l399">   399</a> <span class="sd">    - server_address</span></div>
<div class="parity1 source"><a href="#l400" id="l400">   400</a> <span class="sd">    - RequestHandlerClass</span></div>
<div class="parity0 source"><a href="#l401" id="l401">   401</a> <span class="sd">    - socket</span></div>
<div class="parity1 source"><a href="#l402" id="l402">   402</a> </div>
<div class="parity0 source"><a href="#l403" id="l403">   403</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l404" id="l404">   404</a> </div>
<div class="parity0 source"><a href="#l405" id="l405">   405</a>     <span class="n">address_family</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_INET</span></div>
<div class="parity1 source"><a href="#l406" id="l406">   406</a> </div>
<div class="parity0 source"><a href="#l407" id="l407">   407</a>     <span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_STREAM</span></div>
<div class="parity1 source"><a href="#l408" id="l408">   408</a> </div>
<div class="parity0 source"><a href="#l409" id="l409">   409</a>     <span class="n">request_queue_size</span> <span class="o">=</span> <span class="mi">5</span></div>
<div class="parity1 source"><a href="#l410" id="l410">   410</a> </div>
<div class="parity0 source"><a href="#l411" id="l411">   411</a>     <span class="n">allow_reuse_address</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity1 source"><a href="#l412" id="l412">   412</a> </div>
<div class="parity0 source"><a href="#l413" id="l413">   413</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_address</span><span class="p">,</span> <span class="n">RequestHandlerClass</span><span class="p">,</span> <span class="n">bind_and_activate</span><span class="o">=</span><span class="bp">True</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l414" id="l414">   414</a>         <span class="sd">&quot;&quot;&quot;Constructor.  May be extended, do not override.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l415" id="l415">   415</a>         <span class="n">BaseServer</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">server_address</span><span class="p">,</span> <span class="n">RequestHandlerClass</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l416" id="l416">   416</a>         <span class="bp">self</span><span class="o">.</span><span class="n">socket</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">socket</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">address_family</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l417" id="l417">   417</a>                                     <span class="bp">self</span><span class="o">.</span><span class="n">socket_type</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l418" id="l418">   418</a>         <span class="k">if</span> <span class="n">bind_and_activate</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l419" id="l419">   419</a>             <span class="bp">self</span><span class="o">.</span><span class="n">server_bind</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l420" id="l420">   420</a>             <span class="bp">self</span><span class="o">.</span><span class="n">server_activate</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l421" id="l421">   421</a> </div>
<div class="parity1 source"><a href="#l422" id="l422">   422</a>     <span class="k">def</span> <span class="nf">server_bind</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l423" id="l423">   423</a>         <span class="sd">&quot;&quot;&quot;Called by constructor to bind the socket.</span></div>
<div class="parity1 source"><a href="#l424" id="l424">   424</a> </div>
<div class="parity0 source"><a href="#l425" id="l425">   425</a> <span class="sd">        May be overridden.</span></div>
<div class="parity1 source"><a href="#l426" id="l426">   426</a> </div>
<div class="parity0 source"><a href="#l427" id="l427">   427</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l428" id="l428">   428</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">allow_reuse_address</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l429" id="l429">   429</a>             <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">setsockopt</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">SOL_SOCKET</span><span class="p">,</span> <span class="n">socket</span><span class="o">.</span><span class="n">SO_REUSEADDR</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l430" id="l430">   430</a>         <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">bind</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">server_address</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l431" id="l431">   431</a>         <span class="bp">self</span><span class="o">.</span><span class="n">server_address</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">getsockname</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l432" id="l432">   432</a> </div>
<div class="parity0 source"><a href="#l433" id="l433">   433</a>     <span class="k">def</span> <span class="nf">server_activate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l434" id="l434">   434</a>         <span class="sd">&quot;&quot;&quot;Called by constructor to activate the server.</span></div>
<div class="parity0 source"><a href="#l435" id="l435">   435</a> </div>
<div class="parity1 source"><a href="#l436" id="l436">   436</a> <span class="sd">        May be overridden.</span></div>
<div class="parity0 source"><a href="#l437" id="l437">   437</a> </div>
<div class="parity1 source"><a href="#l438" id="l438">   438</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l439" id="l439">   439</a>         <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">listen</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">request_queue_size</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l440" id="l440">   440</a> </div>
<div class="parity0 source"><a href="#l441" id="l441">   441</a>     <span class="k">def</span> <span class="nf">server_close</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l442" id="l442">   442</a>         <span class="sd">&quot;&quot;&quot;Called to clean-up the server.</span></div>
<div class="parity0 source"><a href="#l443" id="l443">   443</a> </div>
<div class="parity1 source"><a href="#l444" id="l444">   444</a> <span class="sd">        May be overridden.</span></div>
<div class="parity0 source"><a href="#l445" id="l445">   445</a> </div>
<div class="parity1 source"><a href="#l446" id="l446">   446</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l447" id="l447">   447</a>         <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l448" id="l448">   448</a> </div>
<div class="parity0 source"><a href="#l449" id="l449">   449</a>     <span class="k">def</span> <span class="nf">fileno</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l450" id="l450">   450</a>         <span class="sd">&quot;&quot;&quot;Return socket file number.</span></div>
<div class="parity0 source"><a href="#l451" id="l451">   451</a> </div>
<div class="parity1 source"><a href="#l452" id="l452">   452</a> <span class="sd">        Interface required by select().</span></div>
<div class="parity0 source"><a href="#l453" id="l453">   453</a> </div>
<div class="parity1 source"><a href="#l454" id="l454">   454</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l455" id="l455">   455</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">fileno</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l456" id="l456">   456</a> </div>
<div class="parity0 source"><a href="#l457" id="l457">   457</a>     <span class="k">def</span> <span class="nf">get_request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l458" id="l458">   458</a>         <span class="sd">&quot;&quot;&quot;Get the request and client address from the socket.</span></div>
<div class="parity0 source"><a href="#l459" id="l459">   459</a> </div>
<div class="parity1 source"><a href="#l460" id="l460">   460</a> <span class="sd">        May be overridden.</span></div>
<div class="parity0 source"><a href="#l461" id="l461">   461</a> </div>
<div class="parity1 source"><a href="#l462" id="l462">   462</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l463" id="l463">   463</a>         <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">accept</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l464" id="l464">   464</a> </div>
<div class="parity0 source"><a href="#l465" id="l465">   465</a>     <span class="k">def</span> <span class="nf">shutdown_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l466" id="l466">   466</a>         <span class="sd">&quot;&quot;&quot;Called to shutdown and close an individual request.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l467" id="l467">   467</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l468" id="l468">   468</a>             <span class="c">#explicitly shutdown.  socket.close() merely releases</span></div>
<div class="parity0 source"><a href="#l469" id="l469">   469</a>             <span class="c">#the socket and waits for GC to perform the actual close.</span></div>
<div class="parity1 source"><a href="#l470" id="l470">   470</a>             <span class="n">request</span><span class="o">.</span><span class="n">shutdown</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">SHUT_WR</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l471" id="l471">   471</a>         <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l472" id="l472">   472</a>             <span class="k">pass</span> <span class="c">#some platforms may raise ENOTCONN here</span></div>
<div class="parity0 source"><a href="#l473" id="l473">   473</a>         <span class="bp">self</span><span class="o">.</span><span class="n">close_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l474" id="l474">   474</a> </div>
<div class="parity0 source"><a href="#l475" id="l475">   475</a>     <span class="k">def</span> <span class="nf">close_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l476" id="l476">   476</a>         <span class="sd">&quot;&quot;&quot;Called to clean up an individual request.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l477" id="l477">   477</a>         <span class="n">request</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l478" id="l478">   478</a> </div>
<div class="parity0 source"><a href="#l479" id="l479">   479</a> </div>
<div class="parity1 source"><a href="#l480" id="l480">   480</a> <span class="k">class</span> <span class="nc">UDPServer</span><span class="p">(</span><span class="n">TCPServer</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l481" id="l481">   481</a> </div>
<div class="parity1 source"><a href="#l482" id="l482">   482</a>     <span class="sd">&quot;&quot;&quot;UDP server class.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l483" id="l483">   483</a> </div>
<div class="parity1 source"><a href="#l484" id="l484">   484</a>     <span class="n">allow_reuse_address</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity0 source"><a href="#l485" id="l485">   485</a> </div>
<div class="parity1 source"><a href="#l486" id="l486">   486</a>     <span class="n">socket_type</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">SOCK_DGRAM</span></div>
<div class="parity0 source"><a href="#l487" id="l487">   487</a> </div>
<div class="parity1 source"><a href="#l488" id="l488">   488</a>     <span class="n">max_packet_size</span> <span class="o">=</span> <span class="mi">8192</span></div>
<div class="parity0 source"><a href="#l489" id="l489">   489</a> </div>
<div class="parity1 source"><a href="#l490" id="l490">   490</a>     <span class="k">def</span> <span class="nf">get_request</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l491" id="l491">   491</a>         <span class="n">data</span><span class="p">,</span> <span class="n">client_addr</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">recvfrom</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">max_packet_size</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l492" id="l492">   492</a>         <span class="k">return</span> <span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="p">),</span> <span class="n">client_addr</span></div>
<div class="parity0 source"><a href="#l493" id="l493">   493</a> </div>
<div class="parity1 source"><a href="#l494" id="l494">   494</a>     <span class="k">def</span> <span class="nf">server_activate</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l495" id="l495">   495</a>         <span class="c"># No need to call listen() for UDP.</span></div>
<div class="parity1 source"><a href="#l496" id="l496">   496</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l497" id="l497">   497</a> </div>
<div class="parity1 source"><a href="#l498" id="l498">   498</a>     <span class="k">def</span> <span class="nf">shutdown_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l499" id="l499">   499</a>         <span class="c"># No need to shutdown anything.</span></div>
<div class="parity1 source"><a href="#l500" id="l500">   500</a>         <span class="bp">self</span><span class="o">.</span><span class="n">close_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l501" id="l501">   501</a> </div>
<div class="parity1 source"><a href="#l502" id="l502">   502</a>     <span class="k">def</span> <span class="nf">close_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l503" id="l503">   503</a>         <span class="c"># No need to close anything.</span></div>
<div class="parity1 source"><a href="#l504" id="l504">   504</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l505" id="l505">   505</a> </div>
<div class="parity1 source"><a href="#l506" id="l506">   506</a> <span class="k">class</span> <span class="nc">ForkingMixIn</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l507" id="l507">   507</a> </div>
<div class="parity1 source"><a href="#l508" id="l508">   508</a>     <span class="sd">&quot;&quot;&quot;Mix-in class to handle each request in a new process.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l509" id="l509">   509</a> </div>
<div class="parity1 source"><a href="#l510" id="l510">   510</a>     <span class="n">timeout</span> <span class="o">=</span> <span class="mi">300</span></div>
<div class="parity0 source"><a href="#l511" id="l511">   511</a>     <span class="n">active_children</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l512" id="l512">   512</a>     <span class="n">max_children</span> <span class="o">=</span> <span class="mi">40</span></div>
<div class="parity0 source"><a href="#l513" id="l513">   513</a> </div>
<div class="parity1 source"><a href="#l514" id="l514">   514</a>     <span class="k">def</span> <span class="nf">collect_children</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l515" id="l515">   515</a>         <span class="sd">&quot;&quot;&quot;Internal routine to wait for children that have exited.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l516" id="l516">   516</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span> <span class="k">return</span></div>
<div class="parity0 source"><a href="#l517" id="l517">   517</a>         <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="bp">self</span><span class="o">.</span><span class="n">max_children</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l518" id="l518">   518</a>             <span class="c"># XXX: This will wait for any child process, not just ones</span></div>
<div class="parity0 source"><a href="#l519" id="l519">   519</a>             <span class="c"># spawned by this library. This could confuse other</span></div>
<div class="parity1 source"><a href="#l520" id="l520">   520</a>             <span class="c"># libraries that expect to be able to wait for their own</span></div>
<div class="parity0 source"><a href="#l521" id="l521">   521</a>             <span class="c"># children.</span></div>
<div class="parity1 source"><a href="#l522" id="l522">   522</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l523" id="l523">   523</a>                 <span class="n">pid</span><span class="p">,</span> <span class="n">status</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">waitpid</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l524" id="l524">   524</a>             <span class="k">except</span> <span class="n">os</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l525" id="l525">   525</a>                 <span class="n">pid</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l526" id="l526">   526</a>             <span class="k">if</span> <span class="n">pid</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="p">:</span> <span class="k">continue</span></div>
<div class="parity0 source"><a href="#l527" id="l527">   527</a>             <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">pid</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l528" id="l528">   528</a> </div>
<div class="parity0 source"><a href="#l529" id="l529">   529</a>         <span class="c"># XXX: This loop runs more system calls than it ought</span></div>
<div class="parity1 source"><a href="#l530" id="l530">   530</a>         <span class="c"># to. There should be a way to put the active_children into a</span></div>
<div class="parity0 source"><a href="#l531" id="l531">   531</a>         <span class="c"># process group and then use os.waitpid(-pgid) to wait for any</span></div>
<div class="parity1 source"><a href="#l532" id="l532">   532</a>         <span class="c"># of that set, but I couldn&#39;t find a way to allocate pgids</span></div>
<div class="parity0 source"><a href="#l533" id="l533">   533</a>         <span class="c"># that couldn&#39;t collide.</span></div>
<div class="parity1 source"><a href="#l534" id="l534">   534</a>         <span class="k">for</span> <span class="n">child</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l535" id="l535">   535</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l536" id="l536">   536</a>                 <span class="n">pid</span><span class="p">,</span> <span class="n">status</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">waitpid</span><span class="p">(</span><span class="n">child</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">WNOHANG</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l537" id="l537">   537</a>             <span class="k">except</span> <span class="n">os</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l538" id="l538">   538</a>                 <span class="n">pid</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity0 source"><a href="#l539" id="l539">   539</a>             <span class="k">if</span> <span class="ow">not</span> <span class="n">pid</span><span class="p">:</span> <span class="k">continue</span></div>
<div class="parity1 source"><a href="#l540" id="l540">   540</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l541" id="l541">   541</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">pid</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l542" id="l542">   542</a>             <span class="k">except</span> <span class="ne">ValueError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l543" id="l543">   543</a>                 <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s">&#39;</span><span class="si">%s</span><span class="s">. x=</span><span class="si">%d</span><span class="s"> and list=</span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">message</span><span class="p">,</span> <span class="n">pid</span><span class="p">,</span></div>
<div class="parity1 source"><a href="#l544" id="l544">   544</a>                                                            <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="p">))</span></div>
<div class="parity0 source"><a href="#l545" id="l545">   545</a> </div>
<div class="parity1 source"><a href="#l546" id="l546">   546</a>     <span class="k">def</span> <span class="nf">handle_timeout</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l547" id="l547">   547</a>         <span class="sd">&quot;&quot;&quot;Wait for zombies after self.timeout seconds of inactivity.</span></div>
<div class="parity1 source"><a href="#l548" id="l548">   548</a> </div>
<div class="parity0 source"><a href="#l549" id="l549">   549</a> <span class="sd">        May be extended, do not override.</span></div>
<div class="parity1 source"><a href="#l550" id="l550">   550</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l551" id="l551">   551</a>         <span class="bp">self</span><span class="o">.</span><span class="n">collect_children</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l552" id="l552">   552</a> </div>
<div class="parity0 source"><a href="#l553" id="l553">   553</a>     <span class="k">def</span> <span class="nf">process_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l554" id="l554">   554</a>         <span class="sd">&quot;&quot;&quot;Fork a new subprocess to process the request.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l555" id="l555">   555</a>         <span class="bp">self</span><span class="o">.</span><span class="n">collect_children</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l556" id="l556">   556</a>         <span class="n">pid</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">fork</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l557" id="l557">   557</a>         <span class="k">if</span> <span class="n">pid</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l558" id="l558">   558</a>             <span class="c"># Parent process</span></div>
<div class="parity0 source"><a href="#l559" id="l559">   559</a>             <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l560" id="l560">   560</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span> <span class="o">=</span> <span class="p">[]</span></div>
<div class="parity0 source"><a href="#l561" id="l561">   561</a>             <span class="bp">self</span><span class="o">.</span><span class="n">active_children</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">pid</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l562" id="l562">   562</a>             <span class="bp">self</span><span class="o">.</span><span class="n">close_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l563" id="l563">   563</a>         <span class="k">else</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l564" id="l564">   564</a>             <span class="c"># Child process.</span></div>
<div class="parity0 source"><a href="#l565" id="l565">   565</a>             <span class="c"># This must never return, hence os._exit()!</span></div>
<div class="parity1 source"><a href="#l566" id="l566">   566</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l567" id="l567">   567</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">finish_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l568" id="l568">   568</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l569" id="l569">   569</a>                 <span class="n">os</span><span class="o">.</span><span class="n">_exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l570" id="l570">   570</a>             <span class="k">except</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l571" id="l571">   571</a>                 <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l572" id="l572">   572</a>                     <span class="bp">self</span><span class="o">.</span><span class="n">handle_error</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l573" id="l573">   573</a>                     <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l574" id="l574">   574</a>                 <span class="k">finally</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l575" id="l575">   575</a>                     <span class="n">os</span><span class="o">.</span><span class="n">_exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l576" id="l576">   576</a> </div>
<div class="parity0 source"><a href="#l577" id="l577">   577</a> </div>
<div class="parity1 source"><a href="#l578" id="l578">   578</a> <span class="k">class</span> <span class="nc">ThreadingMixIn</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l579" id="l579">   579</a>     <span class="sd">&quot;&quot;&quot;Mix-in class to handle each request in a new thread.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l580" id="l580">   580</a> </div>
<div class="parity0 source"><a href="#l581" id="l581">   581</a>     <span class="c"># Decides how threads will act upon termination of the</span></div>
<div class="parity1 source"><a href="#l582" id="l582">   582</a>     <span class="c"># main process</span></div>
<div class="parity0 source"><a href="#l583" id="l583">   583</a>     <span class="n">daemon_threads</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity1 source"><a href="#l584" id="l584">   584</a> </div>
<div class="parity0 source"><a href="#l585" id="l585">   585</a>     <span class="k">def</span> <span class="nf">process_request_thread</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l586" id="l586">   586</a>         <span class="sd">&quot;&quot;&quot;Same as in BaseServer but as a thread.</span></div>
<div class="parity0 source"><a href="#l587" id="l587">   587</a> </div>
<div class="parity1 source"><a href="#l588" id="l588">   588</a> <span class="sd">        In addition, exception handling is done here.</span></div>
<div class="parity0 source"><a href="#l589" id="l589">   589</a> </div>
<div class="parity1 source"><a href="#l590" id="l590">   590</a> <span class="sd">        &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l591" id="l591">   591</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l592" id="l592">   592</a>             <span class="bp">self</span><span class="o">.</span><span class="n">finish_request</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l593" id="l593">   593</a>             <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l594" id="l594">   594</a>         <span class="k">except</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l595" id="l595">   595</a>             <span class="bp">self</span><span class="o">.</span><span class="n">handle_error</span><span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l596" id="l596">   596</a>             <span class="bp">self</span><span class="o">.</span><span class="n">shutdown_request</span><span class="p">(</span><span class="n">request</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l597" id="l597">   597</a> </div>
<div class="parity1 source"><a href="#l598" id="l598">   598</a>     <span class="k">def</span> <span class="nf">process_request</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l599" id="l599">   599</a>         <span class="sd">&quot;&quot;&quot;Start a new thread to process the request.&quot;&quot;&quot;</span></div>
<div class="parity1 source"><a href="#l600" id="l600">   600</a>         <span class="n">t</span> <span class="o">=</span> <span class="n">threading</span><span class="o">.</span><span class="n">Thread</span><span class="p">(</span><span class="n">target</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">process_request_thread</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l601" id="l601">   601</a>                              <span class="n">args</span> <span class="o">=</span> <span class="p">(</span><span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">))</span></div>
<div class="parity1 source"><a href="#l602" id="l602">   602</a>         <span class="n">t</span><span class="o">.</span><span class="n">daemon</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">daemon_threads</span></div>
<div class="parity0 source"><a href="#l603" id="l603">   603</a>         <span class="n">t</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l604" id="l604">   604</a> </div>
<div class="parity0 source"><a href="#l605" id="l605">   605</a> </div>
<div class="parity1 source"><a href="#l606" id="l606">   606</a> <span class="k">class</span> <span class="nc">ForkingUDPServer</span><span class="p">(</span><span class="n">ForkingMixIn</span><span class="p">,</span> <span class="n">UDPServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l607" id="l607">   607</a> <span class="k">class</span> <span class="nc">ForkingTCPServer</span><span class="p">(</span><span class="n">ForkingMixIn</span><span class="p">,</span> <span class="n">TCPServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l608" id="l608">   608</a> </div>
<div class="parity0 source"><a href="#l609" id="l609">   609</a> <span class="k">class</span> <span class="nc">ThreadingUDPServer</span><span class="p">(</span><span class="n">ThreadingMixIn</span><span class="p">,</span> <span class="n">UDPServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l610" id="l610">   610</a> <span class="k">class</span> <span class="nc">ThreadingTCPServer</span><span class="p">(</span><span class="n">ThreadingMixIn</span><span class="p">,</span> <span class="n">TCPServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l611" id="l611">   611</a> </div>
<div class="parity1 source"><a href="#l612" id="l612">   612</a> <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">socket</span><span class="p">,</span> <span class="s">&#39;AF_UNIX&#39;</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l613" id="l613">   613</a> </div>
<div class="parity1 source"><a href="#l614" id="l614">   614</a>     <span class="k">class</span> <span class="nc">UnixStreamServer</span><span class="p">(</span><span class="n">TCPServer</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l615" id="l615">   615</a>         <span class="n">address_family</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_UNIX</span></div>
<div class="parity1 source"><a href="#l616" id="l616">   616</a> </div>
<div class="parity0 source"><a href="#l617" id="l617">   617</a>     <span class="k">class</span> <span class="nc">UnixDatagramServer</span><span class="p">(</span><span class="n">UDPServer</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l618" id="l618">   618</a>         <span class="n">address_family</span> <span class="o">=</span> <span class="n">socket</span><span class="o">.</span><span class="n">AF_UNIX</span></div>
<div class="parity0 source"><a href="#l619" id="l619">   619</a> </div>
<div class="parity1 source"><a href="#l620" id="l620">   620</a>     <span class="k">class</span> <span class="nc">ThreadingUnixStreamServer</span><span class="p">(</span><span class="n">ThreadingMixIn</span><span class="p">,</span> <span class="n">UnixStreamServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l621" id="l621">   621</a> </div>
<div class="parity1 source"><a href="#l622" id="l622">   622</a>     <span class="k">class</span> <span class="nc">ThreadingUnixDatagramServer</span><span class="p">(</span><span class="n">ThreadingMixIn</span><span class="p">,</span> <span class="n">UnixDatagramServer</span><span class="p">):</span> <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l623" id="l623">   623</a> </div>
<div class="parity1 source"><a href="#l624" id="l624">   624</a> <span class="k">class</span> <span class="nc">BaseRequestHandler</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l625" id="l625">   625</a> </div>
<div class="parity1 source"><a href="#l626" id="l626">   626</a>     <span class="sd">&quot;&quot;&quot;Base class for request handler classes.</span></div>
<div class="parity0 source"><a href="#l627" id="l627">   627</a> </div>
<div class="parity1 source"><a href="#l628" id="l628">   628</a> <span class="sd">    This class is instantiated for each request to be handled.  The</span></div>
<div class="parity0 source"><a href="#l629" id="l629">   629</a> <span class="sd">    constructor sets the instance variables request, client_address</span></div>
<div class="parity1 source"><a href="#l630" id="l630">   630</a> <span class="sd">    and server, and then calls the handle() method.  To implement a</span></div>
<div class="parity0 source"><a href="#l631" id="l631">   631</a> <span class="sd">    specific service, all you need to do is to derive a class which</span></div>
<div class="parity1 source"><a href="#l632" id="l632">   632</a> <span class="sd">    defines a handle() method.</span></div>
<div class="parity0 source"><a href="#l633" id="l633">   633</a> </div>
<div class="parity1 source"><a href="#l634" id="l634">   634</a> <span class="sd">    The handle() method can find the request as self.request, the</span></div>
<div class="parity0 source"><a href="#l635" id="l635">   635</a> <span class="sd">    client address as self.client_address, and the server (in case it</span></div>
<div class="parity1 source"><a href="#l636" id="l636">   636</a> <span class="sd">    needs access to per-server information) as self.server.  Since a</span></div>
<div class="parity0 source"><a href="#l637" id="l637">   637</a> <span class="sd">    separate instance is created for each request, the handle() method</span></div>
<div class="parity1 source"><a href="#l638" id="l638">   638</a> <span class="sd">    can define arbitrary other instance variariables.</span></div>
<div class="parity0 source"><a href="#l639" id="l639">   639</a> </div>
<div class="parity1 source"><a href="#l640" id="l640">   640</a> <span class="sd">    &quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l641" id="l641">   641</a> </div>
<div class="parity1 source"><a href="#l642" id="l642">   642</a>     <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">request</span><span class="p">,</span> <span class="n">client_address</span><span class="p">,</span> <span class="n">server</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l643" id="l643">   643</a>         <span class="bp">self</span><span class="o">.</span><span class="n">request</span> <span class="o">=</span> <span class="n">request</span></div>
<div class="parity1 source"><a href="#l644" id="l644">   644</a>         <span class="bp">self</span><span class="o">.</span><span class="n">client_address</span> <span class="o">=</span> <span class="n">client_address</span></div>
<div class="parity0 source"><a href="#l645" id="l645">   645</a>         <span class="bp">self</span><span class="o">.</span><span class="n">server</span> <span class="o">=</span> <span class="n">server</span></div>
<div class="parity1 source"><a href="#l646" id="l646">   646</a>         <span class="bp">self</span><span class="o">.</span><span class="n">setup</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l647" id="l647">   647</a>         <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l648" id="l648">   648</a>             <span class="bp">self</span><span class="o">.</span><span class="n">handle</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l649" id="l649">   649</a>         <span class="k">finally</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l650" id="l650">   650</a>             <span class="bp">self</span><span class="o">.</span><span class="n">finish</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l651" id="l651">   651</a> </div>
<div class="parity1 source"><a href="#l652" id="l652">   652</a>     <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l653" id="l653">   653</a>         <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l654" id="l654">   654</a> </div>
<div class="parity0 source"><a href="#l655" id="l655">   655</a>     <span class="k">def</span> <span class="nf">handle</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l656" id="l656">   656</a>         <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l657" id="l657">   657</a> </div>
<div class="parity1 source"><a href="#l658" id="l658">   658</a>     <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l659" id="l659">   659</a>         <span class="k">pass</span></div>
<div class="parity1 source"><a href="#l660" id="l660">   660</a> </div>
<div class="parity0 source"><a href="#l661" id="l661">   661</a> </div>
<div class="parity1 source"><a href="#l662" id="l662">   662</a> <span class="c"># The following two classes make it possible to use the same service</span></div>
<div class="parity0 source"><a href="#l663" id="l663">   663</a> <span class="c"># class for stream or datagram servers.</span></div>
<div class="parity1 source"><a href="#l664" id="l664">   664</a> <span class="c"># Each class sets up these instance variables:</span></div>
<div class="parity0 source"><a href="#l665" id="l665">   665</a> <span class="c"># - rfile: a file object from which receives the request is read</span></div>
<div class="parity1 source"><a href="#l666" id="l666">   666</a> <span class="c"># - wfile: a file object to which the reply is written</span></div>
<div class="parity0 source"><a href="#l667" id="l667">   667</a> <span class="c"># When the handle() method returns, wfile is flushed properly</span></div>
<div class="parity1 source"><a href="#l668" id="l668">   668</a> </div>
<div class="parity0 source"><a href="#l669" id="l669">   669</a> </div>
<div class="parity1 source"><a href="#l670" id="l670">   670</a> <span class="k">class</span> <span class="nc">StreamRequestHandler</span><span class="p">(</span><span class="n">BaseRequestHandler</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l671" id="l671">   671</a> </div>
<div class="parity1 source"><a href="#l672" id="l672">   672</a>     <span class="sd">&quot;&quot;&quot;Define self.rfile and self.wfile for stream sockets.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l673" id="l673">   673</a> </div>
<div class="parity1 source"><a href="#l674" id="l674">   674</a>     <span class="c"># Default buffer sizes for rfile, wfile.</span></div>
<div class="parity0 source"><a href="#l675" id="l675">   675</a>     <span class="c"># We default rfile to buffered because otherwise it could be</span></div>
<div class="parity1 source"><a href="#l676" id="l676">   676</a>     <span class="c"># really slow for large data (a getc() call per byte); we make</span></div>
<div class="parity0 source"><a href="#l677" id="l677">   677</a>     <span class="c"># wfile unbuffered because (a) often after a write() we want to</span></div>
<div class="parity1 source"><a href="#l678" id="l678">   678</a>     <span class="c"># read and we need to flush the line; (b) big writes to unbuffered</span></div>
<div class="parity0 source"><a href="#l679" id="l679">   679</a>     <span class="c"># files are typically optimized by stdio even when big reads</span></div>
<div class="parity1 source"><a href="#l680" id="l680">   680</a>     <span class="c"># aren&#39;t.</span></div>
<div class="parity0 source"><a href="#l681" id="l681">   681</a>     <span class="n">rbufsize</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></div>
<div class="parity1 source"><a href="#l682" id="l682">   682</a>     <span class="n">wbufsize</span> <span class="o">=</span> <span class="mi">0</span></div>
<div class="parity0 source"><a href="#l683" id="l683">   683</a> </div>
<div class="parity1 source"><a href="#l684" id="l684">   684</a>     <span class="c"># A timeout to apply to the request socket, if not None.</span></div>
<div class="parity0 source"><a href="#l685" id="l685">   685</a>     <span class="n">timeout</span> <span class="o">=</span> <span class="bp">None</span></div>
<div class="parity1 source"><a href="#l686" id="l686">   686</a> </div>
<div class="parity0 source"><a href="#l687" id="l687">   687</a>     <span class="c"># Disable nagle algorithm for this socket, if True.</span></div>
<div class="parity1 source"><a href="#l688" id="l688">   688</a>     <span class="c"># Use only when wbufsize != 0, to avoid small packets.</span></div>
<div class="parity0 source"><a href="#l689" id="l689">   689</a>     <span class="n">disable_nagle_algorithm</span> <span class="o">=</span> <span class="bp">False</span></div>
<div class="parity1 source"><a href="#l690" id="l690">   690</a> </div>
<div class="parity0 source"><a href="#l691" id="l691">   691</a>     <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l692" id="l692">   692</a>         <span class="bp">self</span><span class="o">.</span><span class="n">connection</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span></div>
<div class="parity0 source"><a href="#l693" id="l693">   693</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">timeout</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l694" id="l694">   694</a>             <span class="bp">self</span><span class="o">.</span><span class="n">connection</span><span class="o">.</span><span class="n">settimeout</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">timeout</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l695" id="l695">   695</a>         <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">disable_nagle_algorithm</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l696" id="l696">   696</a>             <span class="bp">self</span><span class="o">.</span><span class="n">connection</span><span class="o">.</span><span class="n">setsockopt</span><span class="p">(</span><span class="n">socket</span><span class="o">.</span><span class="n">IPPROTO_TCP</span><span class="p">,</span></div>
<div class="parity0 source"><a href="#l697" id="l697">   697</a>                                        <span class="n">socket</span><span class="o">.</span><span class="n">TCP_NODELAY</span><span class="p">,</span> <span class="bp">True</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l698" id="l698">   698</a>         <span class="bp">self</span><span class="o">.</span><span class="n">rfile</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection</span><span class="o">.</span><span class="n">makefile</span><span class="p">(</span><span class="s">&#39;rb&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">rbufsize</span><span class="p">)</span></div>
<div class="parity0 source"><a href="#l699" id="l699">   699</a>         <span class="bp">self</span><span class="o">.</span><span class="n">wfile</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">connection</span><span class="o">.</span><span class="n">makefile</span><span class="p">(</span><span class="s">&#39;wb&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">wbufsize</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l700" id="l700">   700</a> </div>
<div class="parity0 source"><a href="#l701" id="l701">   701</a>     <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l702" id="l702">   702</a>         <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">closed</span><span class="p">:</span></div>
<div class="parity0 source"><a href="#l703" id="l703">   703</a>             <span class="k">try</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l704" id="l704">   704</a>                 <span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l705" id="l705">   705</a>             <span class="k">except</span> <span class="n">socket</span><span class="o">.</span><span class="n">error</span><span class="p">:</span></div>
<div class="parity1 source"><a href="#l706" id="l706">   706</a>                 <span class="c"># An final socket error may have occurred here, such as</span></div>
<div class="parity0 source"><a href="#l707" id="l707">   707</a>                 <span class="c"># the local error ECONNABORTED.</span></div>
<div class="parity1 source"><a href="#l708" id="l708">   708</a>                 <span class="k">pass</span></div>
<div class="parity0 source"><a href="#l709" id="l709">   709</a>         <span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity1 source"><a href="#l710" id="l710">   710</a>         <span class="bp">self</span><span class="o">.</span><span class="n">rfile</span><span class="o">.</span><span class="n">close</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l711" id="l711">   711</a> </div>
<div class="parity1 source"><a href="#l712" id="l712">   712</a> </div>
<div class="parity0 source"><a href="#l713" id="l713">   713</a> <span class="k">class</span> <span class="nc">DatagramRequestHandler</span><span class="p">(</span><span class="n">BaseRequestHandler</span><span class="p">):</span></div>
<div class="parity1 source"><a href="#l714" id="l714">   714</a> </div>
<div class="parity0 source"><a href="#l715" id="l715">   715</a>     <span class="c"># XXX Regrettably, I cannot get this working on Linux;</span></div>
<div class="parity1 source"><a href="#l716" id="l716">   716</a>     <span class="c"># s.recvfrom() doesn&#39;t return a meaningful client address.</span></div>
<div class="parity0 source"><a href="#l717" id="l717">   717</a> </div>
<div class="parity1 source"><a href="#l718" id="l718">   718</a>     <span class="sd">&quot;&quot;&quot;Define self.rfile and self.wfile for datagram sockets.&quot;&quot;&quot;</span></div>
<div class="parity0 source"><a href="#l719" id="l719">   719</a> </div>
<div class="parity1 source"><a href="#l720" id="l720">   720</a>     <span class="k">def</span> <span class="nf">setup</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l721" id="l721">   721</a>         <span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">BytesIO</span></div>
<div class="parity1 source"><a href="#l722" id="l722">   722</a>         <span class="bp">self</span><span class="o">.</span><span class="n">packet</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">socket</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">request</span></div>
<div class="parity0 source"><a href="#l723" id="l723">   723</a>         <span class="bp">self</span><span class="o">.</span><span class="n">rfile</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">packet</span><span class="p">)</span></div>
<div class="parity1 source"><a href="#l724" id="l724">   724</a>         <span class="bp">self</span><span class="o">.</span><span class="n">wfile</span> <span class="o">=</span> <span class="n">BytesIO</span><span class="p">()</span></div>
<div class="parity0 source"><a href="#l725" id="l725">   725</a> </div>
<div class="parity1 source"><a href="#l726" id="l726">   726</a>     <span class="k">def</span> <span class="nf">finish</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div>
<div class="parity0 source"><a href="#l727" id="l727">   727</a>         <span class="bp">self</span><span class="o">.</span><span class="n">socket</span><span class="o">.</span><span class="n">sendto</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">wfile</span><span class="o">.</span><span class="n">getvalue</span><span class="p">(),</span> <span class="bp">self</span><span class="o">.</span><span class="n">client_address</span><span class="p">)</span></div>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

