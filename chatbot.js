(function(){
const RESPONSES = [
  {
    patterns: ['hello','hi','hey','hiya','good morning','good afternoon','good evening','howdy','helo'],
    reply: `Welcome to Casa Nova Interiors. I'm here to help you with any questions about our services, pricing or how to get started.<br><br>What can I help you with today?`,
    quick: ['Our Services','Get a Quote','Contact Us','FAQ']
  },
  {
    patterns: ['service','what do you do','what do you offer','offer','provide','help with'],
    reply: `We offer <strong>8 complete service categories:</strong><br><br>
1. Interior Design & Space Planning<br>
2. Construction & Fit-Out<br>
3. Custom Furniture & Joinery<br>
4. Soft Furnishings & Décor<br>
5. Lighting Design<br>
6. Global Sourcing & Procurement<br>
7. Project Management<br>
8. Property Staging & Real Estate<br><br>
We handle everything end-to-end — one partner, zero gaps.`,
    quick: ['Pricing','How it Works','Book a Consultation','Global Sourcing']
  },
  {
    patterns: ['price','cost','how much','budget','fee','charge','rate','pricing','expensive','affordable'],
    reply: `Every project is unique, so our pricing is tailored to your specific needs, space size and materials chosen.<br><br>We work across a range of budgets — from focused styling projects to full luxury builds.<br><br>The best next step is a <strong>free consultation</strong> where we can understand your vision and give you an accurate quote with no hidden costs.`,
    quick: ['Book a Free Consultation','WhatsApp Us','FAQ - Pricing']
  },
  {
    patterns: ['contact','phone','email','call','reach','whatsapp','number','get in touch'],
    reply: `You can reach us anytime:<br><br>
📞 <strong>Phone / WhatsApp:</strong> +254 716 183011<br>
📧 <strong>Email:</strong> casanovaglobalsourcingltd@gmail.com<br>
📍 <strong>Location:</strong> Karen, Nairobi, Kenya<br>
📸 <strong>Instagram:</strong> @casa_nova_global_interior<br><br>
We typically respond within a few hours!`,
    quick: ['WhatsApp Us Now','Book a Consultation','Our Services']
  },
  {
    patterns: ['location','where','based','nairobi','kenya','address','find you','office'],
    reply: `We are based in <strong>Karen, Nairobi, Kenya 00100</strong>.<br><br>We work across Kenya and are expanding across East Africa. For larger projects, we're open to working internationally — just get in touch to discuss.`,
    quick: ['Contact Us','Our Services','Get a Quote']
  },
  {
    patterns: ['source','sourcing','import','china','india','turkey','uae','europe','international','material','furniture from'],
    reply: `Our global sourcing network covers <strong>6 regions:</strong><br><br>
China — furniture & materials<br>
India — textiles & soft furnishings<br>
Turkey — tiles & stone<br>
UAE — luxury fixtures<br>
Europe — designer lighting<br>
<br>
We handle shipping, customs and delivery to your door.`,
    quick: ['Get a Quote','Our Services','Contact Us']
  },
  {
    patterns: ['how long','timeline','duration','take','weeks','months','time'],
    reply: `Project timelines depend on scope:<br><br>
Styling / soft furnishings: <strong>2–4 weeks</strong><br>
Single room fit-out: <strong>4–8 weeks</strong><br>
Full home renovation: <strong>3–6 months</strong><br>
Large commercial: <strong>6–12 months</strong><br><br>
We provide a detailed timeline at the start of every project.`,
    quick: ['Our Process','Get a Quote','Contact Us']
  },
  {
    patterns: ['process','how does it work','how do you work','steps','start','begin','getting started'],
    reply: `Our process is simple — <strong>5 steps:</strong><br><br>
<strong style="color:#c9a96e">01 Consultation</strong> — we listen to your vision<br>
<strong style="color:#c9a96e">02 Design Concept</strong> — mood boards & 3D layouts<br>
<strong style="color:#c9a96e">03 Sourcing</strong> — premium materials procured globally<br>
<strong style="color:#c9a96e">04 Execution</strong> — skilled team transforms your space<br>
<strong style="color:#c9a96e">05 Handover</strong> — your finished space, delivered<br><br>
Ready to start?`,
    quick: ['Book a Free Consultation','Our Services','FAQ']
  },
  {
    patterns: ['consultation','book','appointment','meeting','schedule','free consult'],
    reply: `We offer a <strong>free initial consultation</strong> — no obligation, just a conversation about your vision and how we can help.<br><br>You can:<br>• Fill in our <a href="index.html#contact" style="color:#c9a96e">contact form</a><br>• WhatsApp us on <a href="https://wa.me/254716183011" target="_blank" style="color:#c9a96e">+254 716 183011</a><br>• Email us at <a href="mailto:casanovaglobalsourcingltd@gmail.com" style="color:#c9a96e">casanovaglobalsourcingltd@gmail.com</a>`,
    quick: ['WhatsApp Us Now','FAQ','Our Services']
  },
  {
    patterns: ['airbnb','short let','rental','serviced','staging','stage'],
    reply: `Yes! Our <strong>Property Staging service</strong> includes full Airbnb furnishing and styling packages.<br><br>We transform properties into beautifully styled spaces that attract more bookings and command higher nightly rates — from sourcing furniture to final styling and photography prep.`,
    quick: ['Get a Quote','Our Services','Contact Us']
  },
  {
    patterns: ['founder','esther','who started','owner','designer','lead designer'],
    reply: `Casa Nova Interiors was founded by <strong style="color:#c9a96e">Esther Nyambura Ngumi</strong>, our Founder & Lead Designer.<br><br>Esther built the company with a vision beyond beautiful spaces — to uplift communities and improve lives through quality design made accessible.<br><br>Her name Esther carries meaning: called to stand in the gap and bring good to others.`,
    quick: ["Read Esther's Story",'Our Services','Contact Us']
  },
  {
    patterns: ['partner','partnership','collaborate','architect','contractor','developer','agent','commission','referral'],
    reply: `We actively welcome partnerships with:<br><br>
• Property developers & real estate companies<br>
• Architects & interior designers<br>
• Construction firms<br>
• Hospitality groups<br>
• Global suppliers & luxury brands<br>
• Investors<br><br>
Get in touch to discuss how we can work together.`,
    quick: ['Contact Us','Get a Quote','FAQ - Partnerships']
  },
  {
    patterns: ['residential','home','house','apartment','villa','luxury home'],
    reply: `Residential design is at the heart of what we do. We create stunning luxury homes — from concept and construction through to custom furniture, lighting and the final décor styling.<br><br>Tell us about your home and we'll bring your vision to life.`,
    quick: ['Get a Quote','Our Services','How it Works']
  },
  {
    patterns: ['office','commercial','corporate','retail','hotel','hospitality','restaurant'],
    reply: `We work across all commercial sectors — <strong>corporate offices, hotels, restaurants, retail spaces</strong> and more.<br><br>Our commercial projects combine striking design with practical functionality. We manage everything from fit-out to furnishing so you can focus on your business.`,
    quick: ['Get a Quote','Our Services','Contact Us']
  },
  {
    patterns: ['faq','question','questions','more info','information','tell me more'],
    reply: `Our <strong>FAQ page</strong> covers everything — services, pricing, process, sourcing, timelines and partnerships.<br><br>Or just ask me anything here and I'll do my best to answer!`,
    quick: ['Visit FAQ Page','Our Services','Contact Us']
  },
  {
    patterns: ['thank','thanks','great','perfect','helpful','awesome','brilliant'],
    reply: `You're very welcome! Is there anything else I can help you with?<br><br>Don't hesitate to reach out — our team is always happy to chat.`,
    quick: ['Get a Quote','Contact Us','Our Services']
  },
  {
    patterns: ['bye','goodbye','see you','later','that\'s all','that is all','done'],
    reply: `Thank you for visiting Casa Nova Interiors!<br><br>When you're ready to start your project, we're here. Have a wonderful day!`,
    quick: ['Get a Quote','Contact Us']
  }
];

const QUICK_ACTIONS = {
  'Our Services': () => window.location.href='services.html',
  'Get a Quote': () => window.location.href='index.html#contact',
  'Book a Consultation': () => window.location.href='index.html#contact',
  'Book a Free Consultation': () => window.location.href='index.html#contact',
  'Contact Us': () => window.location.href='index.html#contact',
  'WhatsApp Us': () => window.open('https://wa.me/254716183011?text=Hi%20Casa%20Nova%20Interiors%2C%20I%20have%20an%20enquiry.','_blank'),
  'WhatsApp Us Now': () => window.open('https://wa.me/254716183011?text=Hi%20Casa%20Nova%20Interiors%2C%20I%20have%20an%20enquiry.','_blank'),
  'FAQ': () => window.location.href='faq.html',
  'FAQ - Pricing': () => window.location.href='faq.html#pricing',
  'FAQ - Partnerships': () => window.location.href='faq.html#partnerships',
  'Visit FAQ Page': () => window.location.href='faq.html',
  'Global Sourcing': () => window.location.href='index.html#sourcing',
  'How it Works': () => window.location.href='index.html#process',
  'Our Process': () => window.location.href='index.html#process',
  "Read Esther's Story": () => window.location.href='founder.html',
};

function getReply(input){
  const lower = input.toLowerCase().trim();
  for(const r of RESPONSES){
    if(r.patterns.some(p => lower.includes(p))) return r;
  }
  return {
    reply: `Thanks for your message! I'm not sure I fully understood that — could you rephrase, or choose one of the options below?<br><br>Or you can <a href="https://wa.me/254716183011" target="_blank" style="color:#c9a96e">WhatsApp us directly</a> for a faster answer.`,
    quick: ['Our Services','Pricing','How it Works','Contact Us']
  };
}

const css = `
#cn-chat-widget *{box-sizing:border-box;font-family:'Inter',sans-serif}
#cn-chat-btn{position:fixed;bottom:2rem;left:2rem;z-index:500;width:56px;height:56px;background:linear-gradient(135deg,#c9a96e,#b8935a);border-radius:50%;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(201,169,110,0.45);transition:transform 0.3s,box-shadow 0.3s}
#cn-chat-btn:hover{transform:scale(1.1);box-shadow:0 6px 30px rgba(201,169,110,0.55)}
#cn-chat-btn svg{width:26px;height:26px;fill:#fff;transition:opacity 0.3s}
#cn-chat-btn .icon-close{display:none}
#cn-chat-btn.open .icon-chat{display:none}
#cn-chat-btn.open .icon-close{display:block}
#cn-chat-bubble{position:fixed;bottom:2rem;left:6rem;z-index:499;background:rgba(8,8,8,0.92);border:1px solid rgba(201,169,110,0.3);padding:12px 16px;max-width:210px;backdrop-filter:blur(12px);opacity:0;transform:translateX(-8px);transition:all 0.4s;pointer-events:none}
#cn-chat-bubble.show{opacity:1;transform:translateX(0);pointer-events:auto}
#cn-chat-bubble p{font-size:12px;color:#f5f0eb;line-height:1.6;margin:0}
#cn-chat-bubble p strong{color:#c9a96e}
#cn-chat-bubble::before{content:'';position:absolute;left:-6px;top:50%;transform:translateY(-50%);width:10px;height:10px;background:rgba(8,8,8,0.92);border-left:1px solid rgba(201,169,110,0.3);border-bottom:1px solid rgba(201,169,110,0.3);transform:translateY(-50%) rotate(45deg)}
#cn-chat-box{position:fixed;bottom:6.5rem;left:2rem;z-index:498;width:360px;max-height:520px;background:#0a0a0a;border:1px solid rgba(201,169,110,0.2);display:flex;flex-direction:column;box-shadow:0 16px 60px rgba(0,0,0,0.6);opacity:0;transform:translateY(12px) scale(0.97);transition:all 0.35s cubic-bezier(0.4,0,0.2,1);pointer-events:none}
#cn-chat-box.open{opacity:1;transform:translateY(0) scale(1);pointer-events:auto}
#cn-chat-header{background:linear-gradient(135deg,#c9a96e,#b8935a);padding:1.1rem 1.4rem;display:flex;align-items:center;gap:12px;flex-shrink:0}
#cn-chat-header-avatar{width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.15);display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0}
#cn-chat-header-info{}
#cn-chat-header-name{font-family:'Playfair Display',serif;font-size:0.9rem;color:#fff;font-weight:400}
#cn-chat-header-status{font-size:9px;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,0.7);margin-top:2px;display:flex;align-items:center;gap:5px}
#cn-chat-header-status::before{content:'';width:5px;height:5px;border-radius:50%;background:#7fff7f;flex-shrink:0}
#cn-chat-messages{flex:1;overflow-y:auto;padding:1.2rem;display:flex;flex-direction:column;gap:10px;scrollbar-width:thin;scrollbar-color:rgba(201,169,110,0.2) transparent}
#cn-chat-messages::-webkit-scrollbar{width:3px}
#cn-chat-messages::-webkit-scrollbar-thumb{background:rgba(201,169,110,0.2);border-radius:2px}
.cn-msg{max-width:86%;animation:cnFadeIn 0.3s ease}
@keyframes cnFadeIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
.cn-msg-bot{align-self:flex-start}
.cn-msg-user{align-self:flex-end}
.cn-msg-bubble{padding:10px 14px;font-size:12.5px;line-height:1.7}
.cn-msg-bot .cn-msg-bubble{background:#141414;border:1px solid rgba(201,169,110,0.1);color:rgba(245,240,235,0.8);border-radius:0 10px 10px 10px}
.cn-msg-user .cn-msg-bubble{background:linear-gradient(135deg,#c9a96e,#b8935a);color:#080808;border-radius:10px 10px 0 10px;font-weight:500}
.cn-msg-time{font-size:9px;color:rgba(245,240,235,0.2);margin-top:4px;letter-spacing:1px}
.cn-msg-bot .cn-msg-time{text-align:left;padding-left:2px}
.cn-msg-user .cn-msg-time{text-align:right;padding-right:2px}
.cn-quick-wrap{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.cn-quick{padding:5px 12px;border:1px solid rgba(201,169,110,0.3);background:transparent;color:#c9a96e;font-size:10.5px;cursor:pointer;transition:all 0.25s;border-radius:0;font-family:'Inter',sans-serif;letter-spacing:0.5px}
.cn-quick:hover{background:#c9a96e;color:#080808;border-color:#c9a96e}
.cn-typing{display:flex;gap:4px;padding:10px 14px;background:#141414;border:1px solid rgba(201,169,110,0.1);align-self:flex-start;border-radius:0 10px 10px 10px}
.cn-typing span{width:5px;height:5px;border-radius:50%;background:#c9a96e;animation:cnDot 1.4s infinite}
.cn-typing span:nth-child(2){animation-delay:.2s}
.cn-typing span:nth-child(3){animation-delay:.4s}
@keyframes cnDot{0%,80%,100%{opacity:0.2;transform:scale(0.8)}40%{opacity:1;transform:scale(1)}}
#cn-chat-input-wrap{padding:0.9rem 1rem;border-top:1px solid rgba(201,169,110,0.1);display:flex;gap:8px;flex-shrink:0;background:#080808}
#cn-chat-input{flex:1;background:#141414;border:1px solid rgba(201,169,110,0.15);padding:9px 12px;font-size:12.5px;color:#f5f0eb;outline:none;font-family:'Inter',sans-serif;transition:border-color 0.3s}
#cn-chat-input:focus{border-color:rgba(201,169,110,0.4)}
#cn-chat-input::placeholder{color:rgba(245,240,235,0.2);font-size:11.5px}
#cn-chat-send{width:36px;height:36px;background:#c9a96e;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.3s;flex-shrink:0}
#cn-chat-send:hover{background:#b8935a}
#cn-chat-send svg{width:16px;height:16px;fill:#080808}
#cn-chat-footer{padding:0.5rem 1rem;font-size:9px;color:rgba(245,240,235,0.15);letter-spacing:1px;text-align:center;border-top:1px solid rgba(201,169,110,0.06);background:#080808;flex-shrink:0}
@media(max-width:480px){
#cn-chat-box{width:calc(100vw - 3rem);left:1.5rem}
#cn-chat-bubble{left:5.5rem;max-width:180px}
}
`;

const html = `
<div id="cn-chat-widget">
  <div id="cn-chat-bubble" class="show">
    <p>Got a question about our <strong>design services?</strong> I'm here to help.</p>
  </div>
  <button id="cn-chat-btn" aria-label="Open chat">
    <svg class="icon-chat" viewBox="0 0 24 24"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>
    <svg class="icon-close" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
  </button>
  <div id="cn-chat-box">
    <div id="cn-chat-header">
      <div id="cn-chat-header-avatar">✦</div>
      <div id="cn-chat-header-info">
        <div id="cn-chat-header-name">Casa Nova Assistant</div>
        <div id="cn-chat-header-status">Online · Typically replies instantly</div>
      </div>
    </div>
    <div id="cn-chat-messages"></div>
    <div id="cn-chat-input-wrap">
      <input id="cn-chat-input" type="text" placeholder="Ask me anything..." maxlength="200" autocomplete="off">
      <button id="cn-chat-send">
        <svg viewBox="0 0 24 24"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
      </button>
    </div>
    <div id="cn-chat-footer">Casa Nova Interiors · Karen, Nairobi, Kenya</div>
  </div>
</div>
`;

// Inject styles
const style = document.createElement('style');
style.textContent = css;
document.head.appendChild(style);

// Inject HTML
const div = document.createElement('div');
div.innerHTML = html;
document.body.appendChild(div);

const btn = document.getElementById('cn-chat-btn');
const box = document.getElementById('cn-chat-box');
const bubble = document.getElementById('cn-chat-bubble');
const messages = document.getElementById('cn-chat-messages');
const input = document.getElementById('cn-chat-input');
const send = document.getElementById('cn-chat-send');

let opened = false;

function now(){
  return new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
}

function addMsg(html, type, quick){
  const msg = document.createElement('div');
  msg.className = `cn-msg cn-msg-${type}`;
  msg.innerHTML = `<div class="cn-msg-bubble">${html}</div><div class="cn-msg-time">${now()}</div>`;
  if(quick && quick.length){
    const wrap = document.createElement('div');
    wrap.className = 'cn-quick-wrap';
    quick.forEach(q=>{
      const b = document.createElement('button');
      b.className = 'cn-quick';
      b.textContent = q;
      b.onclick = ()=>{
        if(QUICK_ACTIONS[q]) QUICK_ACTIONS[q]();
        else sendMsg(q);
      };
      wrap.appendChild(b);
    });
    msg.appendChild(wrap);
  }
  messages.appendChild(msg);
  messages.scrollTop = messages.scrollHeight;
}

function showTyping(){
  const t = document.createElement('div');
  t.className = 'cn-typing';
  t.id = 'cn-typing';
  t.innerHTML = '<span></span><span></span><span></span>';
  messages.appendChild(t);
  messages.scrollTop = messages.scrollHeight;
}

function removeTyping(){
  const t = document.getElementById('cn-typing');
  if(t) t.remove();
}

function sendMsg(text){
  if(!text.trim()) return;
  addMsg(text, 'user');
  input.value = '';
  showTyping();
  setTimeout(()=>{
    removeTyping();
    const r = getReply(text);
    addMsg(r.reply, 'bot', r.quick);
  }, 750 + Math.random()*400);
}

btn.addEventListener('click',()=>{
  const isOpen = box.classList.contains('open');
  if(isOpen){
    box.classList.remove('open');
    btn.classList.remove('open');
    bubble.classList.add('show');
  } else {
    box.classList.add('open');
    btn.classList.add('open');
    bubble.classList.remove('show');
    if(!opened){
      opened = true;
      setTimeout(()=>{
        addMsg(`Hi! I'm the <strong style="color:#c9a96e">Casa Nova</strong> assistant.<br><br>I can help you with questions about our services, pricing, process or how to get started. What would you like to know?`, 'bot', ['Our Services','Pricing','How it Works','Book a Consultation']);
      }, 300);
    }
  }
});

send.addEventListener('click',()=>sendMsg(input.value));
input.addEventListener('keypress',e=>{ if(e.key==='Enter') sendMsg(input.value); });

// Auto-hide bubble after 6s
setTimeout(()=>bubble.classList.remove('show'), 6000);

})();
