from markupsafe import escape
from pip import *

link = """В HTML-документе ссылки определяются так:
<a href='#'>Ссылка</a>
"""

tm = escape(link)  # экранирование
print(tm)  # &lt;a href=&#39;#&#39;&gt;Ссылка&lt;/a&gt;