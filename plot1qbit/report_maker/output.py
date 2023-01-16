#####
#https://stackoverflow.com/a/49016797
import io
import os
import base64
import datetime
import matplotlib.pyplot as plt

from plot1qbit.initiate import newc

import logging
import os
import re, json

special = {"*":"red","|":"green","^":"orange","!":"yellow"}

def code(s):
    for key in special.keys():
        s = s.replace(key, "")
    return s

def color_override(codename):
    for key in special.keys():
        if key in codename:
            return special[key]

def alpha_override(codename):
    if '/' in codename:
        return 0.8 #a comparison
    else:
        return 0.8

def linestyle_override(codename):
    if '/' in codename: # a comparison
        return 'solid'
    else:
        return 'solid'

def linewidth_override(codename):
    if '/' in codename: #a comparison
        return 1.0
    else:
        return 2.0

def resolve_read_params_json(s):
    f = re.sub("_[0-9]*_","_",s)
    logging.info("Reading learning parameters file: {f}")
    return json.loads(open(f,"r").read())

def gif_to_html(filename, full_wide=False):
    with open(filename, 'rb') as F:
        bytes = F.read()
    
    encoded = base64.b64encode(bytes)
    
    wide = "fullwidth" if full_wide else "onethird"
    #url=f"data:image/svg+xml;base64, {encoded.decode('utf-8')}"
    url=f"data:image/gif;base64, {encoded.decode('utf-8')}"
    html = f""" <div class="plotcontainer {wide}">
                <a href="{url}" data-lightbox="plots">
                    <img style="width:100%" src="{url}">
                </a>
                </div>"""
    return html



def fig_to_html(fig, full_wide=False):
    if isinstance(fig, plt.Figure):
        img = io.BytesIO()
        fig.savefig(img, format='png',
                    bbox_inches='tight',
                    dpi=100)
        img.seek(0)
        plt.close(fig)

        encoded = base64.b64encode(img.getvalue())


        wide = "fullwidth" if full_wide else "onethird"
        #url=f"data:image/svg+xml;base64, {encoded.decode('utf-8')}"
        url=f"data:image/png;base64, {encoded.decode('utf-8')}"
        html = f""" <div class="plotcontainer {wide}">
                    <a href="{url}" data-lightbox="plots">
                        <img style="width:100%" src="{url}">
                    </a>
                    </div>"""
        return html
    else:
        print("Argument fig must be of type matplotlib.pyplot.Figure")
        raise NotImplementedError
        
def dict_to_table(info):
    from tabulate import tabulate
    content = f"""<div class='plotcontainer'>"""
    content += tabulate(info.items(), tablefmt='html')
    content += "</div>"
    return content

class TabCollection(object):
    def __init__(self, name):
        self.tabs = {}
        self.tab_order = []
        self.collection_name = name

        self._o_collection_name = f"<div class='tabcollectionparent'><div class='collectionname'><h2>{self.collection_name}</h2></div>"
        self._o_start_tab_collection = "<div class='tabcollection'>"
        self._o_end_tab_collection = "</div></div>"
        self._o_enddiv = "</div>"
        self._o_end_tab = "</div>"
        self._o_br = "</br>"
        
    def _compute_dynamic_strings(self):
        self._o_start_first_tab = f"<div class='singletab' style='width:{int(100/len(self.tabs))}%;'>"
        self._o_start_subsequent_tab = f"<div class='singletab' style='width:{int(100/len(self.tabs))}%;'>"

    def _o_tab_name(self, name):
        return f"<div class='tabname'><h3>{code(name)}</h3></div>"
    
    @property
    def header(self):
       return ""

    def new_tab(self, name):
        self.tab_order.append(name)
        self.tabs[name] = []

    def add_to_tab(self, item, tab_name=None):
        if tab_name is None:
            tab_name = self.tab_order[-1]
        #If it's a plot, convert to HTML
        if isinstance(item, plt.Figure):
            item = fig_to_html(item, full_wide=True)

        if isinstance(item, dict):
            item = dict_to_table(item)



        if isinstance(item, str) and item[-4:]==".gif":
            item = gif_to_html(item)


        self.tabs[tab_name].append(item)


    def write(self):
        self._compute_dynamic_strings()
        s = ""
        s += self._o_collection_name
        s += self._o_start_tab_collection

        for ix,tab in enumerate(self.tab_order):
            if ix==0:
                s+=self._o_start_first_tab
            else:
                s+=self._o_start_subsequent_tab
            s+= self._o_tab_name(name=tab)
            for item in self.tabs[tab]:
                s+=item
            s+=self._o_end_tab

        s += self._o_end_tab_collection
        s += self._o_br
        return s


class Report(object):
    def __init__(self, name, info={}):
        self.info = info
        self.content = []
        self.name = name

    def new_tab_collection(self, name):
        return TabCollection(name)

    @property
    def _o_header(self):
        
        head = "<head>"
        
        with open("/".join(__file__.split('/')[:-1]) + '/style.css', 'r') as C:
            head+= "<style>" + C.read() + "</style>"
        
        with open("/".join(__file__.split('/')[:-1]) + '/jquery-3.6.0.min.js', 'r') as C:
            head+= "<script>" + C.read() + "</script>"

        with open("/".join(__file__.split('/')[:-1]) + '/lightbox.min.css', 'r') as C:
            head+= "<style>" + C.read() + "</style>"

        with open("/".join(__file__.split('/')[:-1]) + '/masonry.pkgd.min.js', 'r') as C:
            head+= "<script>" + C.read() + "</script>"


        head += """
        <script>
			function masonryUpdate() {
					setTimeout(function() {
						var $container = $('.tabcollection');
						$container.masonry('reloadItems');
						$container.masonry();
					},100);


				}
            $(document).ready(function(){
                $('.collectionname').click(function() {
                    $(this).siblings().toggle(50);
					masonryUpdate();
                });
                $('.tabname').click(function() {
                    $(this).siblings().toggle(50);
					masonryUpdate();
                });
                $('.tabcollection').masonry({
                    itemSelector: '.singletab',
                });
            });
        </script>
        </head>\n"""
        return head

    def add_plot(self, plot):
        self.content.append(fig_to_html(plot))

    def add_content(self, content):
        if isinstance(content, TabCollection):
            #if a TabCollection instance is passed, call its write method. 
            self.content.append(content.write())
        elif isinstance(content, plt.Figure):
            self.add_plot(plot=content)
        else:
            self.content.append(content)

    def write(self):
        os.makedirs("./reports", exist_ok=True)
        with open(f'./reports/report_{self.name}.html', 'w') as F:
            F.write("<html>\n")
            F.write(self._o_header)
            F.write("\n<body>\n")

            F.write(f"""<h1>{self.name}</h1>
                        <h3>{self.info.get('description','')}</h3>
                        <hr>""")
            
            from tabulate import tabulate
            F.write("""<h2> Information </h2>
                    <div class='plotcontainer'>""")
            F.write(tabulate(self.info.items(), tablefmt='html'))
            F.write("</div>")



            for c in self.content:
                F.write(c)


            F.write(f"<div class='textline center'>Report generated on {datetime.datetime.now().strftime('%A, %b %d, %Y at %H:%M:%S')}.</div>")
            with open("/".join(__file__.split('/')[:-1]) + '/lightbox.min.js', 'r') as C:
                F.write("<script>" + C.read() + "</script>")
            F.write("""<script>
						lightbox.option({
							'imageFadeDuration': 100,
							'resizeDuration': 100,
                            'fitImagesInViewport': true,
							})
            </script>""")
            F.write('</body></html>')


