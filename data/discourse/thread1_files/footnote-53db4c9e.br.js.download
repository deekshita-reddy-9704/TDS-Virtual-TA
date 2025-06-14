define("discourse/plugins/footnote/initializers/composer",["exports","discourse/lib/plugin-api","discourse-i18n","discourse/plugins/footnote/lib/rich-editor-extension"],(function(t,e,o,n){"use strict"
Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0
t.default={name:"footnotes-composer",initialize(){(0,e.withPluginApi)((t=>{t.registerRichEditorExtension(n.default),t.addComposerToolbarPopupMenuOption({action(t){t.addText(`^[${(0,o.i18n)("footnote.title")}]`)},group:"insertions",icon:"asterisk",label:"footnote.add"})}))}}})),define("discourse/plugins/footnote/initializers/inline-footnotes",["exports","@popperjs/core","discourse/lib/icon-library","discourse/lib/plugin-api"],(function(t,e,o,n){"use strict"
let i
function s(t){const o=document.getElementById("footnote-tooltip"),n=o?.dataset.footnoteId,s=t.target,r=s.dataset.footnoteId
if(i?.destroy(),o?.removeAttribute("data-show"),o?.removeAttribute("data-footnote-id"),!t.target.classList.contains("expand-footnote"))return
if(t.preventDefault(),t.stopPropagation(),n===r)return
const a=o.querySelector(".footnote-tooltip-content")
let d=s.closest(".cooked")
null!=d.dataset.refPostId&&(d=document.querySelector(`article[data-post-id="${d.dataset.refPostId}"] .cooked`))
const l=d.querySelector(r)
a.innerHTML=l.innerHTML,o.dataset.show="",o.dataset.footnoteId=r,i?.destroy(),i=(0,e.createPopper)(s,o,{modifiers:[{name:"arrow",options:{element:o.querySelector("#arrow")}},{name:"preventOverflow",options:{altAxis:!0,padding:5}},{name:"offset",options:{offset:[0,12]}}]})}Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0
t.default={name:"inline-footnotes",initialize(t){t.lookup("service:site-settings").display_footnotes_inline&&(document.body.append(function(){const t=document.createElement("template")
return t.innerHTML='\n    <div id="footnote-tooltip" role="tooltip">\n      <div class="footnote-tooltip-content"></div>\n      <div id="arrow" data-popper-arrow></div>\n    </div>\n  '.trim(),t.content.firstChild}()),window.addEventListener("click",s,!0),(0,n.withPluginApi)("0.8.9",(t=>{t.decorateCookedElement((t=>function(t){const e=t.querySelectorAll("sup.footnote-ref")
e.forEach((t=>{const e=t.querySelector("a")
if(!e)return
const n=document.createElement("a")
n.classList.add("expand-footnote"),n.innerHTML=(0,o.iconHTML)("ellipsis"),n.href="",n.role="button",n.dataset.footnoteId=e.getAttribute("href"),t.after(n)})),e.length&&t.classList.add("inline-footnotes")}(t)),{onlyStream:!0,id:"inline-footnotes"}),t.onPageChange((()=>{i?.destroy()
const t=document.getElementById("footnote-tooltip")
t?.removeAttribute("data-show"),t?.removeAttribute("data-footnote-id")}))})))},teardown(){i?.destroy(),window.removeEventListener("click",s),document.getElementById("footnote-tooltip")?.remove()}}})),define("discourse/plugins/footnote/lib/discourse-markdown/footnotes",["exports"],(function(t){"use strict"
Object.defineProperty(t,"__esModule",{value:!0}),t.setup=function(t){t.registerOptions(((t,e)=>{t.features.footnotes=window.markdownitFootnote&&!!e.enable_markdown_footnotes})),t.allowList(["ol.footnotes-list","hr.footnotes-sep","li.footnote-item","a.footnote-backref","sup.footnote-ref"]),t.allowList({custom(t,e,o){if(("a"===t||"li"===t)&&"id"===e)return!!o.match(/^fn(ref)?\d+$/)}}),window.markdownitFootnote&&t.registerPlugin(window.markdownitFootnote)}})),define("discourse/plugins/footnote/lib/rich-editor-extension",["exports"],(function(t){"use strict"
Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0
const e={nodeViews:{footnote:function(t){let{pmView:{EditorView:e},pmState:{EditorState:o},pmTransform:{StepMap:n}}=t
return class{constructor(t,e,o){this.node=t,this.outerView=e,this.getPos=o,this.dom=document.createElement("div"),this.dom.className="footnote",this.innerView=null}selectNode(){this.dom.classList.add("ProseMirror-selectednode"),this.innerView||this.open()}deselectNode(){this.dom.classList.remove("ProseMirror-selectednode"),this.innerView&&this.close()}open(){const t=this.dom.appendChild(document.createElement("div"))
t.style.setProperty("--footnote-counter",`"${this.#t()}"`),t.className="footnote-tooltip",this.innerView=new e(t,{state:o.create({doc:this.node,plugins:this.outerView.state.plugins.filter((t=>!/^(placeholder|trailing-paragraph)\$.*/.test(t.key)))}),dispatchTransaction:this.dispatchInner.bind(this),handleDOMEvents:{mousedown:()=>{this.outerView.hasFocus()&&this.innerView.focus()}}})}#t(){const t=this.dom.closest(".ProseMirror")?.querySelectorAll(".footnote")
return Array.from(t).indexOf(this.dom)+1}close(){this.innerView.destroy(),this.innerView=null,this.dom.textContent=""}dispatchInner(t){const{state:e,transactions:o}=this.innerView.state.applyTransaction(t)
if(this.innerView.updateState(e),!t.getMeta("fromOutside")){const t=this.outerView.state.tr,e=n.offset(this.getPos()+1)
for(let n=0;n<o.length;n++){const i=o[n].steps
for(let o=0;o<i.length;o++)t.step(i[o].map(e))}t.docChanged&&this.outerView.dispatch(t)}}update(t){if(!t.sameMarkup(this.node))return!1
if(this.node=t,this.innerView){const e=this.innerView.state,o=t.content.findDiffStart(e.doc.content)
if(null!=o){let{a:n,b:i}=t.content.findDiffEnd(e.doc.content),s=o-Math.min(n,i)
s>0&&(n+=s,i+=s),this.innerView.dispatch(e.tr.replace(o,i,t.slice(o,n)).setMeta("fromOutside",!0))}}return!0}destroy(){this.innerView&&this.close()}stopEvent(t){return this.innerView&&this.innerView.dom.contains(t.target)}ignoreMutation(){return!0}}}},nodeSpec:{footnote:{attrs:{id:{}},group:"inline",content:"block*",inline:!0,atom:!0,draggable:!1,parseDOM:[{tag:"div.footnote"}],toDOM:()=>["div",{class:"footnote"},0]}},parse(t){let{pmModel:{Slice:e,Fragment:o}}=t
return{footnote_ref:{node:"footnote",getAttrs:t=>({id:t.meta.id})},footnote_block:{ignore:!0},footnote_open(t,n,i,s){const r=t.top(),a=n.meta.id
let d=i.slice(s+1,i.length-1)
const l=d.findIndex((t=>"footnote_close"===t.type))
d=d.slice(0,l),r.content.forEach(((n,i)=>{const s=[]
n.descendants(((n,i)=>{if("footnote"!==n.type.name||n.attrs.id!==a)return
t.stack=[],t.openNode(t.schema.nodes.footnote),t.parseTokens(d)
const l=t.closeNode()
t.stack=[r]
const c=new e(o.from(l),0,0)
s.push({from:i,to:i+2,slice:c})}))
for(const{from:t,to:e,slice:o}of s)r.content[i]=r.content[i].replace(t,e,o)})),i.splice(s+1,d.length+1)},footnote_anchor:{ignore:!0,noCloseToken:!0}}},serializeNode:{footnote(t,e){if(1===e.content.content.length&&"paragraph"===e.content.firstChild.type.name)t.write("^["),t.renderContent(e.content.firstChild),t.write("]")
else{const o=t.footnoteContents??=[]
o.push(e.content),t.write(`[^${o.length}]`)}},afterSerialize(t){const e=t.footnoteContents
if(e)for(let o=0;o<e.length;o++){const n=t.delim
t.write(`[^${o+1}]: `),t.delim+="    ",t.renderContent(e[o]),t.delim=n}}},inputRules:[{match:/\^\[(.*?)]$/,handler:(t,e,o,n)=>{const i=t.doc.slice(o+2,n).content,s=t.schema.nodes.paragraph.create(null,i),r=t.schema.nodes.footnote.create(null,s)
return t.tr.replaceWith(o,n,r)}}]}
t.default=e}))

//# sourceMappingURL=footnote-8e40c022.map