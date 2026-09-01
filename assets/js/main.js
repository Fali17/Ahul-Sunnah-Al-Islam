
function openMenu(){ document.getElementById('header-nav').classList.add('menu-open'); document.getElementById('openMenu').style.display='none'; document.getElementById('closeMenu').style.display='block'; }
function closeMenu(){ document.getElementById('header-nav').classList.remove('menu-open'); document.getElementById('openMenu').style.display='block'; document.getElementById('closeMenu').style.display='none'; }
(function(){
  var doc=document.documentElement, prog=document.getElementById('readProgress'), btt=document.getElementById('backToTop'), yr=document.getElementById('year');
  if(yr) yr.textContent=new Date().getFullYear();
  window.addEventListener('scroll', function(){
    var sc=(doc.scrollTop/(doc.scrollHeight-doc.clientHeight))*100;
    if(prog) prog.style.width=sc+'%';
    if(btt){ if(doc.scrollTop>500) btt.classList.add('show'); else btt.classList.remove('show'); }
  },{passive:true});
  if(btt) btt.addEventListener('click', function(){ window.scrollTo({top:0,behavior:'smooth'}); });
})();
 // POSTS.JSON based prev/next for single pages
async function initPostNav(){
  const navEl = document.getElementById('postNav');
  if(!navEl) return;
  try{
    const res = await fetch('/posts.json');
    const posts = await res.json();
    const currentPath = location.pathname;
    const idx = posts.findIndex(p => currentPath.includes(p.id) || currentPath.endsWith(p.url) || ('/'+p.url) === currentPath);
    if(idx===-1) return;
    let html='';
    if(idx>0) html+=`<a class="prev-btn" href="/${posts[idx-1].url}">Previous<br><span>${posts[idx-1].title}</span></a>`;
    if(idx<posts.length-1) html+=`<a class="next-btn" href="/${posts[idx+1].url}">Next<br><span>${posts[idx+1].title}</span></a>`;
    navEl.innerHTML=html;
    navEl.style.display='flex';
  }catch(e){ console.log('nav error',e); }
}
document.addEventListener('DOMContentLoaded', initPostNav);
