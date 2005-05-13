# a utility pythonscript for zwikis
# to be called in the context of the wiki folder..
# you might need to put the folder id before objectValues
# in some vhost setups ? please report

<dtml-var standard_html_header>
<dtml-let 
 p="objectValues('ZWiki Page')[0]"
 pagetypes="['stx','rst','moin','html','plaintext']"
 >

<h2>Wiki pages by type</h2>
<p>
<ul>
<dtml-in pagetypes prefix=a>
<li> <a href="#&dtml-a_item;">&dtml-a_item;</a>: <dtml-var "_.len(p.pages(page_type=a_item))">
</dtml-in>
<li> total: <dtml-var "p.pageCount()">
</ul>

<dtml-in pagetypes prefix=a>
<a name="&dtml-a_item;"><h2>&dtml-a_item; pages</h2></a>
<p>
<dtml-in "p.pages(page_type=a_item)" prefix=b>
- <a href="&dtml-id;">&dtml-Title;</a>
</dtml-in>
</dtml-in>


</dtml-let>
<dtml-var standard_html_footer>
