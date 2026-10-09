from pathlib import Path
from xml.sax.saxutils import escape
import cairosvg, math
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]; A=ROOT/'assets'; A.mkdir(parents=True,exist_ok=True)
K='#090909'; K2='#101010'; K3='#151515'; WHITE='#F1EEE8'; MUTED='#AAA7A1'; DIM='#777570'; HAIR='#343330'; GOLD='#CEBA97'; UNDER='#211F1C'

def e(s): return escape(str(s))
def svg_begin(w,h): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">\n'
def rect(x,y,w,h,fill='none',stroke='none',r=0,sw=1): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'
def line(x1,y1,x2,y2,col=HAIR,sw=1,dash=None): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{col}" stroke-width="{sw}" fill="none"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def circle(cx,cy,r,fill='none',stroke='none',sw=1): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'
def txt(x,y,text,size=18,col=WHITE,weight=400,family='Inter, Arial, sans-serif',tracking=None,anchor=None):
 return f'<text x="{x}" y="{y}" fill="{col}" font-family="{family}" font-size="{size}" font-weight="{weight}"'+(f' letter-spacing="{tracking}"' if tracking is not None else '')+(f' text-anchor="{anchor}"' if anchor else '')+f'>{e(text)}</text>\n'
def label(x,y,s,sz=13,col=MUTED,tracking=2.6): return txt(x,y,s,sz,col,600,'Inter, Arial, sans-serif',tracking)
def save(name,body,w,h):
 content=svg_begin(w,h)+f'<title>{e(name.replace("-"," "))}</title>\n'+body+'</svg>'
 (A/f'{name}.svg').write_text(content,encoding='utf-8')
 cairosvg.svg2png(bytestring=content.encode(),write_to=str(A/f'{name}.png'),output_width=w,output_height=h)

W=1120
# ── HERO / an editorial title rather than a science-fiction illustration ──
s=rect(0,0,1120,437,K)+rect(1,1,1118,435,'none',HAIR,3)
s+=rect(44,38,8,8,GOLD)+label(67,47,'IFBILAL / ENGINEERING PORTFOLIO',12,WHITE,2.35)+txt(1070,47,'2026 / 01',12,DIM,600,tracking=2,anchor='end')
s+=line(44,70,1076,70)
s+=txt(51,180,'BILAL',113,WHITE,750,tracking=-6)
s+=txt(51,291,'TAHIR',113,WHITE,750,tracking=-6)
s+=rect(390,260,13,13,GOLD, r=0) # restrained sign-off square
s+=label(55,337,'FULL-STACK AI ENGINEER',20,GOLD,2.55)
s+=txt(54,376,'Agentic AI  /  Computer vision  /  Software engineering',17,MUTED)
s+=line(630,105,630,382,HAIR)
# right, clear hierarchy with architecture-style column
s+=label(677,131,'WHAT I DO',14,DIM,2.45)
for y,n,head,sub in [(174,'01','REASON','Multi-agent systems & RAG'),(244,'02','PERCEIVE','Detection & multimodal ML'),(314,'03','SHIP','APIs, interfaces & deployments')]:
 s+=label(677,y,n,12,GOLD,1.2)+txt(723,y,head,21,WHITE,650,tracking=0.4)
 s+=txt(723,y+24,sub,15,MUTED)
 if y!=314:s+=line(677,y+40,1069,y+40,HAIR)
s+=line(44,403,1076,403)
s+=label(46,426,'FAST-NUCES · ISLAMABAD',11,DIM,1.6)+txt(1072,426,'RESEARCH → SYSTEMS → PRODUCT',11,DIM,600,tracking=1.55,anchor='end')
s+=circle(1040,116,3,GOLD)+circle(1040,116,11,'none',HAIR,1)
s+='<circle cx="1040" cy="116" r="5" fill="none" stroke="#CEBA97" opacity="0.65"><animate attributeName="r" values="5;14;5" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.65;0;0.65" dur="5s" repeatCount="indefinite"/></circle>'
save('hero',s,1120,437)

# ── PROJECTS, as typographic dossiers ──

def outer_project(n,field,title,subtitle,skills,scheme):
 s=rect(0,0,1120,211,K2)+rect(1,1,1118,209,'none',HAIR,2)
 s+=label(42,41,n+'  /  '+field,12,DIM,2.25)
 s+=txt(41,105,title,49,WHITE,690,tracking=-2)
 s+=txt(43,143,subtitle,16,MUTED)
 s+=line(42,161,635,161,HAIR)
 s+=label(42,189,' · '.join(skills),12,GOLD,1.05)
 s+=line(673,30,673,181,HAIR)
 s+=scheme
 s+=txt(1078,188,'↗',24,GOLD,400,anchor='end')
 return s

# SkyEye: simplified physical detection pipeline
s=''
s+=label(713,43,'CONFIDENCE-GATED INFERENCE',10,DIM,1.6)
s+=rect(713,65,109,50,K3,HAIR,3)+label(730,86,'IMAGE',11,WHITE,1.2)+txt(730,101,'RGB / IR',11,MUTED)
s+=line(822,90,847,90,GOLD,2)+circle(846,90,3,GOLD)
s+=rect(851,65,99,50,K3,HAIR,3)+label(867,86,'YOLO',11,WHITE,1.4)+txt(867,101,'DETECTOR',10,MUTED)
s+=line(950,90,969,90,GOLD,2)+circle(968,90,3,GOLD)
s+=rect(974,65,101,50,K3,HAIR,3)+label(989,86,'VLM',11,WHITE,1.4)+txt(989,101,'FALLBACK',10,MUTED)
s+=line(899,115,899,135,DIM,1)+line(899,135,1028,135,DIM,1)+line(1028,135,1028,115,DIM,1)
s+=txt(727,160,'94.11% RGB mAP50',14,WHITE,600)+label(942,159,'RESEARCH EVAL.',10,DIM,1.1)
save('project-skyeye',outer_project('01','COMPUTER VISION','SkyEye','Detect, evaluate, and escalate uncertain predictions.',['YOLO','VLMs','FastAPI','Docker'],s),1120,211)

# Rahnuma: source/merit/response
s=''
s+=label(710,42,'A GROUNDED ANSWER PATH',10,DIM,1.5)
for x,y,w,t,sub in [(718,65,144,'RETRIEVAL','Cited sources'),(900,65,149,'CALCULATION','Exact merit')]:
 s+=rect(x,y,w,54,K3,HAIR,3)+label(x+15,y+23,t,10,WHITE,1.35)+txt(x+15,y+43,sub,12,MUTED)
s+=line(789,119,789,144,HAIR)+line(975,119,975,144,HAIR)+line(789,144,975,144,HAIR)
s+=line(881,144,881,157,GOLD,1.5)+circle(881,144,4,GOLD)
s+=label(775,184,'VERIFIABLE ANSWER',12,GOLD,1.65)
save('project-rahnuma',outer_project('02','AGENTIC SYSTEMS','Rahnuma','Admissions guidance grounded in sources and exact logic.',['LangGraph','pgvector','FastAPI','Next.js'],s),1120,211)

# CodeGrapher: graph structure with structural nodes, grays only
s=''
s+=label(715,40,'QUERYABLE CODEBASE MAP',10,DIM,1.6)
P=[(737,90),(817,67),(825,133),(911,100),(996,64),(1017,143)]
for a,b in [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(3,5),(4,5)]:
 s+=line(*P[a],*P[b],HAIR,2)
for i,(x,y) in enumerate(P):
 s+=circle(x,y,10,K3,GOLD if i in (2,3) else DIM,1.4)+circle(x,y,2.7,GOLD if i in (2,3) else MUTED)
s+=line(720,169,1063,169,HAIR)+label(720,190,'AST  /  DEPENDENCIES  /  IMPACT ANALYSIS',11,GOLD,1.1)
save('project-codegrapher',outer_project('03','CODE INTELLIGENCE','CodeGrapher','Understand repositories as structure, not just text.',['CrewAI','Neo4j','Tree-Sitter','Qdrant'],s),1120,211)

# Real estate: literal small form outline
s=''
s+=label(713,37,'SELLER WORKFLOW / PRE-QUALIFICATION',10,DIM,1.3)
s+=rect(716,54,347,117,K3,HAIR,5)+rect(731,68,317,13,UNDER)+circle(742,74,3,GOLD)+circle(754,74,3,DIM)+circle(766,74,3,DIM)
s+=rect(733,94,124,9,HAIR, r=2)+rect(733,112,94,8,HAIR,r=2)+rect(733,128,145,8,HAIR,r=2)
s+=rect(905,93,124,49,'none',HAIR,4)+label(919,112,'AI REVIEW',10,GOLD,1)
s+=line(919,122,1016,122,HAIR,3)+line(919,131,987,131,HAIR,3)
s+=rect(733,151,296,4,GOLD)
save('project-real-estate',outer_project('04','AI + PRODUCT','Real Estate Intake','A complete seller workflow with useful AI touchpoints.',['Next.js','Supabase','Groq','TypeScript'],s),1120,211)

# ── Stack taxonomy; a compact visual index with honest substance ──
s=rect(0,0,1120,264,K2)+rect(1,1,1118,262,'none',HAIR,3)
s+=label(38,36,'TOOLBOX / SELECTED TECHNOLOGIES',12,DIM,2.05)
rows=[('01','AI & INFERENCE','PyTorch  /  Transformers  /  LangGraph  /  CrewAI  /  YOLO  /  RAG'),('02','SYSTEMS & DATA','FastAPI  /  PostgreSQL  /  Redis  /  Celery  /  Docker  /  pgvector'),('03','PRODUCT & WEB','TypeScript  /  Next.js  /  React  /  Tailwind  /  Supabase  /  Vercel')]
for i,(num,head,tools) in enumerate(rows):
 y=78+i*66
 if i:s+=line(38,y-27,1082,y-27,HAIR)
 s+=circle(53,y-1,14,'none',HAIR,1.2)
 if i==0:
  s+=circle(53,y-1,5,'none',GOLD,1.1)+circle(53,y-1,1.5,GOLD)
 elif i==1:
  s+=line(46,y-5,60,y-5,GOLD,1.8)+line(46,y,60,y,GOLD,1.8)+line(46,y+5,57,y+5,GOLD,1.8)
 else:
  s+=rect(46,y-7,14,12,'none',GOLD,2)+line(46,y-2,60,y-2,GOLD,1)
 s+=label(81,y+4,head,15,WHITE,1.3)
 s+=txt(417,y+4,tools,16,MUTED)
save('toolbox',s,1120,264)

# ── Evidence / timeline card ──
s=rect(0,0,1120,192,K)+rect(1,1,1118,190,'none',HAIR,3)
s+=label(39,38,'RESEARCH / EVALUATED, NOT GUESSED',12,DIM,2)
metrics=[('94.11%','RGB mAP50','YOLOv12x / evaluation'),('15,552','THERMAL / IR IMAGES','Standardized dataset'),('04','ZERO-SHOT VLMs','Evaluated side by side'),('4×','DEAN’S LIST','FAST-NUCES')]
for i,(value,k,desc) in enumerate(metrics):
 x=40+i*274
 if i:s+=line(x-15,53,x-15,166,HAIR)
 s+=txt(x,104,value,46,WHITE,670,tracking=-1.5)
 s+=label(x,130,k,12,GOLD,1.15)+txt(x,155,desc,12,MUTED)
save('evidence',s,1120,192)

# ── Distinct close: a clean statement, without pulsing neon elements ──
s=rect(0,0,1120,103,K2)+rect(1,1,1118,101,'none',HAIR,3)
s+=rect(39,30,7,7,GOLD)+txt(62,43,'Build the model. Engineer the system. Ship the product.',20,WHITE,630)
s+=label(62,75,'MUHAMMAD BILAL TAHIR  /  @IFBILAL',11,DIM,1.6)
s+=label(1075,70,'EOF.',13,GOLD,1.5)
save('footer',s,1120,103)

# ── Compact social links; self-contained, no remote image providers ──
for name,head,sub,mark in [('contact-github','GITHUB','@IfBilal','>_'),('contact-linkedin','LINKEDIN','m-bilaltahir','in'),('contact-email','EMAIL','Get in touch','@')]:
 ss=rect(0,0,330,64,K2)+rect(1,1,328,62,'none',HAIR,3)
 ss+=rect(17,16,32,32,'none',HAIR,4)+txt(33,37,mark,16,GOLD,750,anchor='middle')
 ss+=label(64,28,head,12,WHITE,1.4)+txt(64,47,sub,12,MUTED)
 ss+=txt(310,40,'↗',20,GOLD,400,anchor='end')
 save(name,ss,330,64)

# ── Quiet animated motion; locally hosted GIF, no third-party API ──
fontreg='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
fontbold='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
fr=ImageFont.truetype(fontreg,19); fs=ImageFont.truetype(fontreg,14); fb=ImageFont.truetype(fontbold,14)
phrases=['AGENTS THAT CAN CITE THEIR SOURCES','VISION SYSTEMS THAT KNOW WHEN TO DEFER','FROM PROTOTYPE TO DEPLOYABLE SOFTWARE']
frames=[]
for j in range(3):
 for f in range(12):
  im=Image.new('RGB',(1120,77),K2); d=ImageDraw.Draw(im)
  d.rectangle((0,0,1119,76),outline=HAIR,width=1)
  d.rectangle((29,31,37,39),fill=GOLD if f%12 in (0,1,2,3,4,5,6,7,8,9) else DIM)
  d.text((53,29),'IN PROGRESS',font=fb,fill=WHITE)
  d.line((225,17,225,60),fill=HAIR,width=1)
  msg=phrases[j]
  # smooth reveal 2/3 cycle, then linger
  chars=min(len(msg),max(0,round((f/8)*len(msg))))
  d.text((258,27),msg[:chars],font=fr,fill=WHITE)
  if f<10 and (f//2)%2==0:
   endx=258+int(d.textlength(msg[:chars],font=fr)); d.rectangle((endx+3,26,endx+15,50),fill=GOLD)
  # restrained progress indicator
  for k in range(3):d.rectangle((1028+k*18,36,1038+k*18,40),fill=GOLD if k==j else HAIR)
  frames.append(im)
frames[0].save(A/'focus.gif',save_all=True,append_images=frames[1:],duration=115,loop=0,optimize=True)

# Compose proof-of-direction artwork: not pretending to be GitHub full rendered page.
names=['hero','project-skyeye','project-rahnuma','project-codegrapher','project-real-estate','toolbox','evidence','footer']
imgs=[Image.open(A/(x+'.png')).convert('RGB') for x in names]
scale=.75; pad=23; gap=16
parts=[x.resize((int(x.width*scale),int(x.height*scale)),Image.Resampling.LANCZOS) for x in imgs]
wide=parts[0].width+pad*2; high=pad*2+sum(x.height for x in parts)+gap*(len(parts)-1)
coll=Image.new('RGB',(wide,high),'#080808')
y=pad
for part in parts:coll.paste(part,(pad,y)); y+=part.height+gap
coll.save(ROOT.parent/'IfBilal-Black-Edition-Preview.png',quality=95)
print('built:',[(x.name,x.stat().st_size) for x in A.iterdir()])
