
/* 

  ================================================
  PVII Horizontal Gallery scripts
  Copyright (c) 2006 Project Seven Development
  www.projectseven.com
  Version: 1.1.5
  ================================================
  
*/

var p7gsiem=(navigator.appVersion.indexOf("MSIE 5")>-1&&navigator.userAgent.indexOf("Mac")>-1)?true:false;
var p7gsca,p7gsa=new Array(),p7gsplot=new Array(),p7gstmb = new Array();
function P7_setHGS(){
	var i,d='',tA,h="<sty"+"le type=\"text/css\">";
	if(!document.getElementById){
		return;
	}
	tA=navigator.userAgent.toLowerCase();
	if(window.opera){
		if(tA.indexOf("opera 5")>-1 || tA.indexOf("opera 6")>-1){
			return;
		}
	}
	h+="#p7GS{visibility:hidden;}";
	h+="<"+"/sty"+"le>";
	document.write(h);
}
P7_setHGS();
function P7_HGSinit(){
	var i,x,s,vp,sc,ul,li,h,hh=0,w,ww=0,uw,n,nn,im,a,nv,hv,bh,bw,ed,eh,ew,cv,j,kw,tA;
	if(!document.getElementById){
		return;
	}
	tA=navigator.userAgent.toLowerCase();
	if(window.opera){
		if(tA.indexOf("opera 5")>-1 || tA.indexOf("opera 6")>-1){
			return;
		}
	}
	p7gsa=arguments;
	if(p7gsiem||tA.indexOf('scape6/6')>-1){
		p7gsa[1]=0;
	}
	vp=document.getElementById('p7GSvp');
	sc=document.getElementById('p7GSsc');
	li=sc.getElementsByTagName('LI');
	im=sc.getElementsByTagName('IMG');
	for(i=0;i<im.length;i++){
		im[i].style.display='block';
	}
	for(i=0;i<li.length;i++){
		li[i].style.position='absolute';
		h=li[i].offsetHeight;
		w=li[i].offsetWidth;
		hh=(h>hh)?h:hh;
		ww=(w>ww)?w:ww;
	}
	for(i=0;i<li.length;i++){
		li[i].style.height=hh+'px';
		li[i].style.width=ww+'px';
	}
	for(i=0;i<li.length;i++){
		h=li[i].offsetHeight;
		w=li[i].offsetWidth;
		if(h>hh){
			n=hh-(h-hh);
			li[i].style.height=n+'px';
		}
		if(w>ww){
			n=ww-(w-ww);
			li[i].style.width=n+'px';
		}
	}
	ul=sc.getElementsByTagName('UL');
	ww=0;
	for(i=0;i<ul.length;i++){
		li=ul[i].getElementsByTagName('LI');
		kw=0;
		for(j=0;j<li.length;j++){
			w=li[j].offsetWidth;
			h=li[j].offsetHeight;
			li[j].style.left=kw+'px';
			kw+=w;
			ww=(kw>ww)?kw:ww;
		}
		ul[i].style.position='relative';
		ul[i].style.height=h+'px';
	}
	if(ul.length==1){
		document.getElementById('p7GSnv').style.display='none';
	}
	sc.style.position='absolute';
	sc.style.top='0px';
	sc.style.left='0px';
	vp.style.height=h+'px';
	vp.style.width=ww+'px';
	vp.style.overflow='hidden';
	if(p7gsa[0]==1){
		li=sc.getElementsByTagName('LI');
		for(i=0;i<li.length;i++){
			im=li[i].getElementsByTagName('IMG')[0];
			h=im.offsetHeight;
			w=im.offsetWidth;
			hh=parseInt(li[i].style.height);
			ww=parseInt(li[i].style.width);
			n=parseInt((hh-h)/2);
			nn=parseInt((ww-w)/2);
			if(n>0){
				im.style.marginTop=n+'px';
			}
			if(nn>0){
				im.style.marginLeft=nn+'px';
			}
		}
	}
	document.p7gspre=new Array();
	a=sc.getElementsByTagName('A');
	x=0;
	for(i=0;i<a.length;i++){
		if(a[i].parentNode.nodeName=='LI'){
			a[i].onmouseover=function(){
				P7_HGSover(this);
			};
			a[i].onfocus=function(){
				P7_HGSover(this);
			};
			a[i].onmouseout=function(){
				P7_HGSout(this);
			};
a[i].onclick= function(){
	return P7_HGSshow(this);
};
document.p7gspre[x]=new Image();
document.p7gspre[x].cmp=false;
document.p7gspre[x].onload=function (){
	this.cmp=true;
};
a[i].p7gsindex=x;
p7gstmb[x]=a[i];
x++;
}
}
nv=document.getElementById('p7GSnv');
x=0;
if(nv){
hv=nv.innerHTML;
ul=sc.getElementsByTagName('UL');
for(i=0;i<ul.length;i++){
s=(i===0)?'':' <span>|</span> ';
x=i+1;
hv+=s+'<a id="p7gsn'+x+'" href="javascript:;" title="View Thumbnail Panel '+x+'">'+x+'</a>';
}
nv.innerHTML=hv;
a=nv.getElementsByTagName('A');
for(i=0;i<a.length;i++){
a[i].onclick= function(){
	return P7_HGSnvs(this);
};
}
}
document.getElementById('p7GS').style.visibility="visible";
h=p7gsa[4];
if(!P7_HGSurl()){
if(h>0){
P7_HGStrig(h-1,9);
}
}
}
function P7_HGSover(a){
	var im=a.getElementsByTagName('IMG')[0];
	if(im.className!='p7GSon'){
		im.className='p7GSover';
	}
}
function P7_HGSout(a){
	var im=a.getElementsByTagName('IMG')[0];
	if(im.className!='p7GSon'){
		im.className='';
	}
}
function P7_HGSnvs(a,g){
	var i,p,ta;
	p=parseInt(a.id.replace('p7gsn',''));
	g=(g)?g:0;
	ta=document.getElementById('p7GSnv').getElementsByTagName('A');
	for(i=0;i<ta.length;i++){
		if(ta[i].className){
			ta[i].className='';
		}
	}
	a.className='p7GSnvon';
	P7_HGSmove(p,g);
	return false;
}
function P7_HGSmove(p,g){
	var i,h,sc,t,c,m;
	sc=document.getElementById('p7GSsc');
	h=sc.getElementsByTagName('LI')[0].offsetHeight;
	t=((h*p)-h)*-1;
	c=parseInt(sc.style.top);
	c=(c)?c:0;
	m=(c<t)?1:0;
	P7_HGSvon();
	if(p7gsa[5]==1&&g!=9&&g!=6){
		P7_HGSscr(t,m);
	}
	else{
		sc.style.top=t+'px';
		P7_HGSvoff();
	}
}
function P7_HGSvoff(){
	var ta,i,j,ul,m=false;
	ta=document.getElementById('p7GSnv').getElementsByTagName('A');
	for(i=0;i<ta.length;i++){
		if(ta[i].className=='p7GSnvon'){
			m=true;
			break;
		}
	}
	if(m){
		ul=document.getElementById('p7GSsc').getElementsByTagName('UL');
		for(j=0;j<ul.length;j++){
			if(j==i){
				ul[j].style.visibility='visible';
			}
			else{
				ul[j].style.visibility='hidden';
			}
		}
	}
}
function P7_HGSvon(){
	var i,ul=document.getElementById('p7GSsc').getElementsByTagName('UL');
	for(i=0;i<ul.length;i++){
		ul[i].style.visibility='visible';
	}
}
function P7_HGSscr(t,m){
	var d,r,y=30;
	d=document.getElementById('p7GSsc');
	c=parseInt(d.style.top);
	r=P7_HGSrate(c,t);
	c+=(m==1)?r:r*-1;
	if(m==1){
		c=(c>=t)?t:c;
	}
	else{
		c=(c<=t)?t:c;
	}
	d.style.top=c+"px";
	if(c!=t){
		d.p7hgsan=setTimeout("P7_HGSscr("+t+","+m+")",y);
	}
	else{
		P7_HGSvoff();
	}
}
function P7_HGSrate(c,t){
	var tt=Math.abs(t-c),i=parseInt(tt*0.08,10);
	i=(i<=20)?20:i;
	return i;
}
function P7_HGStrig(n,ug){
	var i,sc,a,f;
	ug=(ug)?ug:0;
	a=p7gstmb[n];
	if(a){
		P7_HGStrigp(a,ug);
		f=P7_HGSshow(a,ug);
	}
}
function P7_HGStrigp(a,ug){
	var i,nv,ul,pp,f;
	nv=document.getElementById('p7GSnv').getElementsByTagName('A');
	ul=document.getElementById('p7GSsc').getElementsByTagName('UL');
	pp=a.parentNode;
	while(pp){
		if(pp.nodeName=='UL'){
			break;
		}
		pp=pp.parentNode;
	}
	for(i=0;i<ul.length;i++){
		if(ul[i]==pp){
			break;
		}
	}
	f = P7_HGSnvs(nv[i],ug);
}
function P7_HGSurl(){
	var i,h,s,x,m=false,p='pic';
	if(document.getElementById){
		h=document.location.search;
		if(h){
			h=h.replace('?','');
			s=h.split('=');
			if(s&&s.length){
				for(i=0;i<s.length;i+=2){
					if(s[i]==p){
						x=parseInt(s[i+1]);
						if(x){
							P7_HGStrig(x,9);
							m=true;
							break;
						}
					}
				}
			}
		}
		h=document.location.hash;
		if(h){
			x=parseInt(h.substring(1,h.length));
			if(x&&x>0){
				m=true;
			}
		}
	}
	if(m){
		x--;
		P7_HGStrig(x,9);
	}
	return m;
}
function P7_HGSshow(a,ug){
	var i,ti,im,fM,pM,dM,cM,dD,ds,h,w;
	ug=(ug)?ug:0;
	im=a.getElementsByTagName('IMG')[0];
	ti=document.getElementById('p7GSvp').getElementsByTagName('IMG');
	if(p7gsca){
		if(p7gsca==a){
			return false;
		}
	}
	for(i=0;i<ti.length;i++){
		ti[i].className='';
	}
	im.className='p7GSon';
	dM=document.getElementById('p7GSfs');
	fM=dM.getElementsByTagName('IMG')[0];
	pM=document.p7gspre[a.p7gsindex];
	if(document.p7gswait){
		clearTimeout(document.p7gswait);
	}
	p7gsca=a;
	if(!pM.cmp){
		P7_GSpbs(fM);
		pM.src=a.href;
		P7_GSwait(a.p7gsindex,ug);
	}
	else{
		P7_GSfin(pM,ug);
	}
	return false;
}
function P7_GSpbs(im,ug){
	var i,l,t,p,pb,pw,ph,ih,iw;
	pb=document.getElementById('p7GSpb');
	pw=pb.offsetWidth;
	ph=pb.offsetHeight;
	if(im){
		ih=(p7gsiem)?im.height:im.offsetHeight;
		iw=(p7gsiem)?im.width:im.offsetWidth;
		t=(ih-ph)/2;
		l=(iw-pw)/2;
		p=P7_getPos(im);
		l+=p[0];
		t+=p[1];
		pb.style.left=l+'px';
		pb.style.top=t+'px';
		pb.style.visibility="visible";
	}
}
function P7_getPos(im){
	var p,pp,l=0,t=0,r=new Array(2);
	pp=im;
	while(pp){
		l+=(pp.offsetLeft)?pp.offsetLeft:0;
		t+=(pp.offsetTop)?pp.offsetTop:0;
		if(window.opera||navigator.userAgent.indexOf("Safari")>-1){
			if(pp.nodeName=="BODY"){
				l-=(pp.offsetLeft)?pp.offsetLeft:0;
				t-=(pp.offsetTop)?pp.offsetTop:0;
			}
		}
		pp=pp.offsetParent;
	}
	if(p7gsiem){
		l+=parseInt(document.body.currentStyle.marginLeft);
		t+=parseInt(document.body.currentStyle.marginTop);
	}
	r[0]=l;
	r[1]=t;
	return r;
}
function P7_GSwait(ix,ug){
	var im=document.p7gspre[ix];
	if(im.cmp || (!document.all&&im.height>1)){
		im.cmp=true;
		document.getElementById('p7GSpb').style.visibility='hidden';
		P7_GSfin(im,ug);
	}
	else{
		document.p7gswait=setTimeout("P7_GSwait("+ix+","+ug+")",200);
	}
}
function P7_GSfin(im,ug){
	var dM,fM,cM,aL,cD,ds,tB,dT='',tH='',aC,fS,an,st='',h,h1,h2,ti,ci,ct,cn;
	an=p7gsa[1];
	if(an>0){
		st=' style="visibility:hidden"';
	}
	fS=document.getElementById('p7GSfs');
	dM=document.getElementById('p7GSfs');
	fM=dM.getElementsByTagName('IMG')[0];
	tB=p7gsca.getElementsByTagName('IMG')[0];
	tH+='<table class="p7GSfst" align="center" cellpadding="0" cellspacing="0">';
	aL=tB.getAttribute("alt");
	ci=P7GSgi();
	ci[4]+=1;
	ct=p7gstmb.length;
	cn='';
	if(p7gsa[7]==1){
		cn=' <span class="p7GScounter">('+ci[4]+' of '+ct+')</span>';
	}
	aC='<tr><td class="p7GSfsc"><p>'+aL+cn+'</p></td></tr>';
	ds=p7gsca.parentNode.getElementsByTagName('DIV');
	if(ds&&ds[0]){
		dT=ds[0].innerHTML;
	}
	if(p7gsa[2]==1){
		if(aL&&aL.length>0){
			tH+=aC;
		}
	}
	tH+='<tr><td class="p7GSfsi"><i'+'mg s'+'rc="'+im.src+'" alt="'+aL+'"'+st+'></td></tr>';
	if(p7gsa[2]==2){
		if(aL&&aL.length>0){
			tH+=aC;
		}
	}
	if(p7gsa[3]==1){
		if(dT.length>0){
			tH+='<tr><td class="p7GSfsd"><div>'+dT+'</div></td></tr>';
		}
	}
	tH+='</table>';
	dM.innerHTML=tH;
	if(fS){
		fS.style.display='block';
	}
	if(ug<7){
		if(an==1||an==2){
			P7_GSfan();
		}
		else if(an>2){
			P7_GSfie();
		}
	}
	else{
		document.getElementById('p7GSfs').getElementsByTagName('IMG')[0].style.visibility='visible';
	}
}
function P7GSgi(){
	var i,x,a,gi=new Array();
	x=p7gstmb.length-1;
	for(i=0;i<p7gstmb.length;i++){
		if(p7gstmb[i]==p7gsca){
			break;
		}
	}
	gi[0]=0;
	gi[1]=(i>0)?i-1:0;
	gi[2]=(i<x)?i+1:x;
	gi[3]=x;
	gi[4]=i;
	return gi;
}
function P7_GSfie(){
	var i,d,im,f,ff,pim,g=new Array(),an=p7gsa[1];
	im=document.getElementById('p7GSfs').getElementsByTagName('IMG')[0];
	pim=im.parentNode;
	if(!im.parentNode.filters){
		p7gsa[1]=1;
		P7_GSfan();
		return;
	}
	f='progid:DXImageTransform.Microsoft.';
	d=' Duration=1';
	g[0]='Fade';
	g[1]='Fade';
	g[2]='Fade';
	g[3]='Fade';
	g[4]='Iris(irisstyle="SQUARE", motion="in"'+d+')';
	g[5]='Iris(irisstyle="SQUARE", motion="out"'+d+')';
	g[6]='Iris(irisstyle="CIRCLE", motion="in"'+d+')';
	g[7]='Iris(irisstyle="CIRCLE", motion="out"'+d+')';
	g[8]='Blinds(direction="up", bands=1'+d+')';
	g[9]='Blinds(direction="down", bands=1'+d+')';
	g[10]='Blinds(direction="right", bands=1'+d+')';
	g[11]='Blinds(direction="left", bands=1'+d+')';
	g[12]='Blinds(direction="right"'+d+')';
	g[13]='Blinds(direction="down"'+d+')';
	g[14]='CheckerBoard(direction="right"'+d+')';
	g[15]='CheckerBoard(direction="down"'+d+')';
	g[16]='RandomDissolve('+d+')';
	g[17]='Barn(orientation="vertical", motion="in"'+d+')';
	g[18]='Barn(orientation="vertical", motion="out"'+d+')';
	g[19]='Barn(orientation="horizontal", motion="in"'+d+')';
	g[20]='Barn(orientation="horizontal", motion="out"'+d+')';
	g[21]='Strips(motion="leftdown"'+d+')';
	g[22]='Strips(motion="leftup"'+d+')';
	g[23]='Strips(motion="rightdown"'+d+')';
	g[24]='Strips(motion="rightup"'+d+')';
	g[25]='RandomBars(orientation="horizontal"'+d+')';
	g[26]='RandomBars(orientation="vertical"'+d+')';
	g[27]='Wipe(GradientSize=1.0, wipeStyle=0, motion="forward"'+d+')';
	g[28]='Inset()';
	g[29]='Pixelate(MaxSquare=50,Duration=1,Enabled=false'+d+')';
	g[30]='RadialWipe(wipeStyle="clock"'+d+')';
	g[31]='RadialWipe(wipeStyle="wedge"'+d+')';
	g[32]='RadialWipe(wipeStyle="radial"'+d+')';
	g[33]='Slide(slideStyle="PUSH", bands=1'+d+')';
	g[34]='Slide(slideStyle="SWAP", bands=5'+d+')';
	g[35]='Slide(slideStyle="HIDE", bands=2'+d+')';
	g[36]='Spiral(GridSizeX=16, GridSizeY=16'+d+')';
	g[37]='Stretch(stretchStyle="hide"'+d+')';
	g[38]='Stretch(stretchStyle="spin"'+d+')';
	g[39]='Stretch(stretchStyle="push"'+d+')';
	g[40]='Wheel(spokes=4'+d+')';
	g[41]='Wheel(spokes=16'+d+')';
	g[42]='zigzag(GridSizeX=8, GridSizeY=8'+d+')';
	an=(an>g.length)?3:an;
	f+=g[an];
	pim.style.filter=f;
	if(pim.filters.length<1){
		p7gsa[1]=1;
		P7_GSfan();
		return;
	}
	pim.filters[0].Apply();
	im.style.visibility='visible';
	pim.filters[0].Play();
}
function P7_GSfan(){
	var im,fh,fw,tB,tF,tL,l,t,dt,dl,df,fr,dn,pl,an,c=10,i,ih,iw,ih2,iw2,l2,t2,lm=false,tm=false,ch=c,cw=c;
	an=p7gsa[1];
	im=document.getElementById('p7GSfs').getElementsByTagName('IMG')[0];
	tF=P7_getPos(im);
	fh=im.offsetHeight;
	fw=im.offsetWidth;
	tB=p7gsca.getElementsByTagName('IMG')[0];
	tD=P7_getPos(tB);
	if(an==1){
		l=parseInt((tB.offsetWidth/2))-5+tD[0];
		t=parseInt((tB.offsetHeight/2))-5+tD[1];
	}
	else{
		l=parseInt((fw/2))-5+tF[0];
		t=parseInt((fh/2))-5+tF[1];
	}
	tL=document.getElementById('p7GSah');
	tL.innerHTML='<img src="'+im.src+'" height="'+c+'" width="'+c+'">';
	tL.style.left=l+'px';
	tL.style.top=t+'px';
	dt=tF[1]-t;
	dl=tF[0]-l;
	fr=20;
	p7gsplot.length=0;
	ih=fh-c;
	iw=fw-c;
	if(ih>iw){
		dn=parseInt(ih/fr)+1;
		ih2=fr;
		iw2=parseInt(iw/dn)+1;
	}
	else{
		dn=parseInt(iw/fr)+1;
		iw2=fr;
		ih2=parseInt(ih/dn)+1;
	}
	l2=parseInt( Math.abs(dl)/dn)+1;
	if(dl<0){
		l2=l2*-1;
		lm=true;
	}
	t2=parseInt( Math.abs(dt)/dn)+1;
	if(dt<0){
		t2=t2*-1;
		tm=true;
	}
	for(i=1;i<dn+1;i++){
		t+=t2;
		if(tm){
			t=(t<=tF[1])?tF[1]:t;
		}
		else{
			t=(t>=tF[1])?tF[1]:t;
		}
		l+=l2;
		if(lm){
			l=(l<=tF[0])?tF[0]:l;
		}
		else{
			l=(l>=tF[0])?tF[0]:l;
		}
		cw+=iw2;
		cw=(cw>=fw)?fw:cw;
		ch+=ih2;
		ch=(ch>=fh)?fh:ch;
		p7gsplot[i-1]=t+','+l+','+cw+','+ch;
	}
	tL.style.visibility="visible";
	P7_GSfanim(0);
}
function P7_GSfanim(p){
	var i,pl,dy=10,tL=document.getElementById('p7GSah'),im=tL.getElementsByTagName('IMG')[0];
	if(p<p7gsplot.length){
		pl=p7gsplot[p].split(',');
		tL.style.top=pl[0]+'px';
		tL.style.left=pl[1]+'px';
		im.style.width=pl[2]+'px';
		im.style.height=pl[3]+'px';
		p++;
		setTimeout("P7_GSfanim("+p+")",dy);
	}
	else{
		document.getElementById('p7GSfs').getElementsByTagName('IMG')[0].style.visibility='visible';
		tL.style.visibility='hidden';
	}
}
