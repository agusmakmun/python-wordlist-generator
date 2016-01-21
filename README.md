# Python-Wordlist-Generator
Creating Awesome Wordlist with Python<br />
update: see <b><a href="https://github.com/agusmakmun/Python-Wordlist-Generator/blob/master/Wordlist%20Generator%20v0.2.py">Wordlist Generator v0.2.py</a></b>, with support 2 method:

1. Real Complete Characters
2. Complete Chars from Input

<blockquote>
If you want getting with first method, we recommend to you use <code>min_length</code> and <code>max_length</code> as same as with max-length. example use: <code>min_length: 4</code> and <code>max-length: 4</code>.
</blockquote>

<pre>
"""
Name            : Python Wordlist Generator
Created By      : Agus Makmun (Summon Agus)
Blog            : bloggersmart.net - python.web.id
Documentation   : https://github.com/agusmakmun/Python-Wordlist-Generator/
License         : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Thanks to       : falsetru - http://stackoverflow.com/a/21559115
"""
</pre>

For output, you can check sample this file: <a href='https://github.com/agusmakmun/Python-Wordlist-Generator/blob/master/wordlist.txt' target='_blank'>wordlist.txt</a>

This script was modified from this thread: http://stackoverflow.com/a/21559115

question for: Python - how to generate wordlist from given characters of specific length

So in this time, we have an idea for modified it with <code>string characters</code> in the module string.
And then output <code>wordlist.txt</code> for that output minimum to maximum length words.

Have awesome creation, with minimum and maximum creation.
For example:
<h5>For 1 length method:</h5>
<pre>
min_length, max_length = 1, 1
</pre>

Then Output:
<pre>
0
1
2
3
...
~
</pre>

<h5>For 2 length method:</h5>
<pre>
min_length, max_length = 1, 2
</pre>

Then Output:
<pre>
0
1
2
3
...
~~
</pre>

Then with awesome this script, you can creating awesome wordlist with minimun to maximum length output words.
