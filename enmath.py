from urllib import request
from bs4 import BeautifulSoup
import re
import codecs

temp=[]
for i in range(0,16):
    temp.append('''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content=" Free Responsive Html5 Templates" />
    
	<title>{{title}}</title>
	
	<!-- Bootstrap core CSS -->
	<link rel="stylesheet" href="css/bootstrap.min.css">
	
    <!-- Custom Fonts -->
	<link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
        
    <!-- Custom styles for this template -->
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" type="text/css" href="css/style-responsive">
    
	
	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="template/js/html5shiv.js"></script>
        <script src="template/js/respond.min.js"></script>
    <![endif]-->
	
</head>

<body>
    <!--header start-->
	<header class="header">
		<div class="sidebar-toggle-box">
			<div class="fa fa-bars tooltips" data-placement="right"></div>
		</div>
		<!--logo start-->
		<a href="#" class="logo"><strong>上海大学</strong></a>
		<!--logo end-->
		
		<div class="top-menu">
			<ul class="nav pull-right top-menu">
				<li><a class="social" href="#">登录</a></li>
			</ul>
		</div>
	</header>
	<!--header end-->
	<!--sidebar start-->
	<aside>
		<div id="sidebar"  class="nav-collapse ">
			<!-- sidebar menu start-->
			<ul class="sidebar-menu">
				<li>
					<a href="index.html">
						<i class="fa fa-tags"></i>首页</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>本系概况</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>
						<span>机构设置</span></a></li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>师资队伍</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>科学研究</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>人才培养</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>国际交流</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>安全宣传</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>联系我们</a>
				</li>
				<li>
					<a href="archive.html">
						<i class="fa fa-tags"></i>登录</a>
				</li>
				<li>
					<a href="indexen.html">
						<i class="fa fa-tags"></i>English</a>
				</li>
			</ul>
		  <!-- sidebar menu end-->
		</div>
	</aside>
    <!--sidebar end-->
	
	
	
	
	<!--main content start-->
	<section id="main-content">
		<section class="wrapper">
			<div class="post-thumbnail" style="">
				<img width="100%" height="auto"src="images/10.jpg">
			</div>
			<div class="site-inner">
				<div class="site-content">
					<article>
						<div class="art-content">
							<div class="heading text-center">
								<h2>{{title}}</h2>
								<hr class="line">
							</div>
							<div class="excerpt"><p>{{font0}}</p></div>
							<p>{{font1}}</p>
							
							<p>{{font2}}</p>
							
							<p>{{font3}}</p>
							
							<p>{{font4}}</p>
							
							<p>{{font5}}</p>
							
							<p>{{font6}}</p>
							
							<p>{{font7}}</p>
							
							<p>{{font8}}</p>
							
							<p>{{font9}}</p>
							
							<p>{{font10}}</p>
						</div>
					</article>
				</div>
		  </div>
		</section><!-- /wrapper -->
	</section><!-- /MAIN CONTENT -->
	
	<!--main content end-->
	<!--footer start-->
	<footer class="site-footer">
	  <div class="text-center">
		 <div align="center">2019 版权所有 @ 上海大学数学系  沪ICP备09014157   地址：上海市宝山区上大路99号（周边交通）   邮编：200444 <a href="http://www.shu.edu.cn/dhcx.htm" title="电话查询" target="_blank">电话查询</a> 
		           技术支持：上海大学信息化工作办公室   <a href="info@shu.edu.cn" title="info@shu.edu.cn" target="_blank">联系我们</a>           
                 </div>
	  </div>
	</footer>
	<!--footer end-->
	
	
	<!-- js placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.nicescroll.js"></script>
	
    <!--common script for all pages-->
    <script src="js/common-scripts.js"></script>

</body>
</html>''')

template='''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
   
    
	<title>Shanghai University</title>
	
	<!-- Bootstrap core CSS -->
	<link rel="stylesheet" href="css/bootstrap.min.css">
	
    <!-- Custom Fonts -->
	<link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
        
    <!-- Custom styles for this template -->
    <link rel="stylesheet" type="text/css" href="css/style.css">
	<link rel="stylesheet" type="text/css" href="css/style-responsive.css">
	<link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css"> 
	<link rel="stylesheet" href="css/metisMenu.css"> 
	
	<script src="js/jquery.js"></script> 
	<script src="js/bootstrap.min.js"></script> 
	<script src="js/metisMenu.min.js"></script> 
	<script type="text/javascript">
$(function() {
    $('#side-menu').metisMenu(); // ul.nav#side-menu
})
</script>
    
	
	<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="template/js/html5shiv.js"></script>
        <script src="template/js/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
<!--
.STYLE1 {font-size:24px
	font-weight: bold;
	color: #FFFFFF;
}
.STYLE2 {font-size: 10px}
.STYLE3 {color: #F0F0F0}
.header-text1 {
    font-size:18px;
    position: absolute;
    bottom: 0px;
    left: 0px;
    z-index: 1000;
    opacity: 0.7;
}
.sideNav
{
    padding: 10px 0;
    position: fixed;
    left: 0px;
    top: 0px;
    bottom: 0px;
    width:210px; /* same as .content left */
    background-color: #fff;
    border-right: 1px solid #000; 
    z-index: 10;
	color:0,0,0,0;
}
/* ul.sidebar-menu {
    background-color: #222;
}
a, a:hover, a:focus {
    background-color: #222;
}
ul {
    background-color: #222;
}*/
-->
    </style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>

<body style="background-color:#222">
   <!--header start-->
	<header class="header">
		<div class="sidebar-toggle-box">
			<div class="fa fa-bars tooltips" data-placement="right"></div>
		</div>
		<!--logo start-->
		<a href="#" class="logo"><strong>Shanghai University</strong></a>
		<!--logo end-->
		
		<div class="top-menu">
			<ul class="nav pull-right top-menu">
				<li><a class="social" href="#">Login</a></li>
			</ul>
		</div>
	</header>
	<!--header end-->
	<!--sidebar start-->
	<aside>
	<div class="sideNav" role="navigation" style="position:absolute; background-color:rgba(0,0,0,0); border-right:0px">
		<div id="sidebar"  class="nav-collapse ">
			<!-- sidebar menu start-->
			<ul class="sidebar-menu" id="side-menu">
				<li>
                    <a href="#"><i class="fa fa-tags"></i>Home</a>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Overview<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">Historical Evolution</a>
                        </li>
                        <li>
                            <a href="#">Teachers Strenth</a>
                        </li>
						<li>
							<a href="#">Personnel Training</a>
						</li>
						<li>
							<a href="#">Scientific Research</a>
						</li>
                    </ul>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Organization<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">Party & government organizations</a>
                        </li>
                        <li>
                            <a href="#">Academic Committe</a>
                        </li>
						  <li>
                            <a href="#">Teaching Steering Committee</a>
                        </li>
						 <li>
                            <a href="#">Teaching & Researching Institutes</a>
                        </li>
                    </ul>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Faculty<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">Professors</a>
                        </li>
						  <li>
                            <a href="#">Associate Professors</a>
                        </li>
						 <li>
                            <a href="#">Lecturers</a>
                        </li>
						 <li>
                            <a href="#">Honorary/Part-time Professors</a>
                        </li>
						 <li>
                            <a href="#">Postdoctoral</a>
                        </li>
					</ul>
				 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Research<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">Leading Persons</a>
                        </li>
                        <li>
                            <a href="#">Discipline construction</a>
                        </li>
						  <li>
                            <a href="#">Research Institutes</a>
                        </li>
						 <li>
                            <a href="#">Academic Journals</a>
                        </li>
						 <li>
                            <a href="#">Scientific Research Projects</a>
                        </li>
						 <li>
                            <a href="#">Research Papers</a>
                        </li>
						<li>
                            <a href="#">Research Fields</a>
                        </li>
						<li>
                            <a href="#">Academic Publications</a>
                        </li>
						<li>
                            <a href="#">Rewards for Scientic Research</a>
                        </li>
                    </ul>
                 </li>
				 
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Int'l Exchange<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">International Coorperation</a>
                        </li>
                        <li>
                            <a href="#">International Conference</a>
                        </li>
                    </ul>
                 </li>
				  <li>
                    <a href="#"><i class="fa fa-tags"></i>Talents Cultivation<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="#">Occupation Introduction</a>
                        </li>
                        <li>
                            <a href="#">Undergraduate Program</a>
                        </li>
						  <li>
                            <a href="#">Disciplinary Competition</a>
                        </li>
						 <li>
                            <a href="#">Postgraduate Education</a>
                        </li>
						 <li>
                            <a href="#">Undergraduate Education</a>
                        </li>
						 <li>
                            <a href="#">Practical Workstation</a>
                        </li>
                    </ul>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>Contact Us</a>
                 </li>
				 <li>
                    <a href="index.html"><i class="fa fa-tags"></i>中文版</a>
                 </li>
			</ul>
		  <!-- sidebar menu end-->
		</div>
		</div>
	</aside>
    <!--sidebar end-->
	
	
	
	<!--main content start-->
	<section id="main-content">
		<section class="wrapper">
			<!-- Carousel -->
			<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
				
				<!-- Wrapper for slides -->
				<div class="carousel-inner">
					<div class="item active">
						<img src="images/1.jpg" alt="First slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<h2>Department of Mathematics</h2>
								<p class="STYLE1" style="font-size:20px">College of Science, Shanghai University</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="images/1_2.jpg" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">Memorandum of Understanding between Division of Mathematical Sciences-NTU & Math. Dept.-SHU</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="images/1_3.jpg" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">The 5th Sino-Korea Conference on Coding Theory and Its Related Topics</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="images/1_4.jpg" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">Agreement of Cooperation between Math. Dept.-Hong Kong Baptist University & Math. Dept.-Shanghai University</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="images/1_5.jpg" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">2017 International Workshop on Quantum Information, Quantum Computing and Quantum Control</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="images/1_6.jpg" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">2017 International Conference on Matrix Inequalities and Matrix Equations</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
				</div>
				<!-- Controls -->
				<a class="left carousel-control" href="#carousel-example-generic" data-slide="prev">
					<span class="glyphicon glyphicon-chevron-left"></span>
				</a>
				<a class="right carousel-control" href="#carousel-example-generic" data-slide="next">
					<span class="glyphicon glyphicon-chevron-right"></span>
				</a>
			</div><!-- /carousel -->
			
			<div class="no-gutter">
				<div class="col-lg-6">
					<article class="box-shadow">
						<div class="no-gutter">
							<div class="col-sm-6 fix-right">
								<img src="images/4.jpg">
							</div>
							<div class="col-sm-6">
								<div class="art-content text-center">
									<div class="heading">
										<h2>News</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2"><a href="ensingle0.html">{{font0}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle1.html">{{font1}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle2.html">{{font2}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle3.html">{{font3}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle4.html">{{font4}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle5.html">{{font5}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle6.html">{{font6}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle7.html">{{font7}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle8.html">{{font8}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle9.html">{{font9}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle10.html">{{font10}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle11.html">{{font11}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle12.html">{{font12}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle13.html">{{font13}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle14.html">{{font14}}</a></p>
									<p align="left" class="STYLE2"><a href="ensingle15.html">{{font15}}</a></p>
								</div>
							</div>
						</div>
					</article>
				</div>
				<div class="col-lg-6">
					<article  class="box-shadow">
					  <div class="no-gutter">
							<div class="col-sm-12">
								<div class="art-content text-center">
									<div class="heading">
										<h2>Links</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2"><a href="{{link1}}">{{title1}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link2}}">{{title2}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link3}}">{{title3}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link4}}">{{title4}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link5}}">{{title5}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link6}}">{{title6}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link7}}">{{title7}}</p>
									<p align="left" class="STYLE2"><a href="{{link8}}">{{title8}}</p>
									<p align="left" class="STYLE2"><a href="{{link9}}">{{title9}}</p>
									<p align="left" class="STYLE2"><a href="{{link10}}">{{title10}}</p>
									<p align="left" class="STYLE2"><a href="{{link11}}">{{title11}}</p>
									<p align="left" class="STYLE2"><a href="{{link12}}">{{title12}}</p>
									<p align="left" class="STYLE2"><a href="{{link13}}">{{title13}}</p>
									<p align="left" class="STYLE2"><a href="{{link14}}">{{title14}}</p>
									<p align="left" class="STYLE2"><a href="{{link15}}">{{title15}}</p>
									<p align="left" class="STYLE2"><a href="{{link16}}">{{title16}}</p>
									<p align="left" class="STYLE2"><a href="{{link17}}">{{title17}}</p>
									<p align="left" class="STYLE2"><a href="{{link18}}">{{title18}}</p>
								</div>
							</div>
						    </div>
					</article>
				</div>
			</div>
		</section><!-- /wrapper -->
	</section><!-- /MAIN CONTENT -->
	
	<!--main content end-->
	<!--footer start-->
	<footer class="site-footer">
	  <div class="text-center">
		         <div align="center">2019 CopyRight @ Shanghai University  沪ICP备09014157   Address: 99 Shangda road, Baoshan District, Shnaghai.(traffic)   Zip Code:200444 <a href="http://www.shu.edu.cn/dhcx.htm" title="Tel." target="_blank">Tel.</a> 
		           Techinical Support:LiYang, ZhangRuiCheng, XuLiuJun, SHU Dept. of Math   <a href="info@shu.edu.cn" title="info@shu.edu.cn" target="_blank">Contact Us</a>           
                 </div>
	  </div>
	</footer>
	<!--footer end-->
	
	
	<!-- js placed at the end of the document so the pages load faster -->
	<script src="js/jquery.nicescroll.js"></script>
	
    <!--common script for all pages-->
    <script src="js/common-scripts.js"></script>

</body>
</html>'''

def content(string):
    res = request.urlopen('http://en.math.shu.edu.cn/')
    soup = BeautifulSoup(res, 'html.parser')
    ListUrls = soup.find_all('a',href=re.compile(string))
    return ListUrls

def printadd(ListUrls):
    global template
    for i in range(0, len(ListUrls)):
        List = ListUrls[i]
        title = List.string
        if List.get('href').startswith('http'):
            href = List.get('href')
        else:
            href = 'http://en.math.shu.edu.cn' + List.get('href')
        template = template.replace("{{link" + str(i+1) + "}}", href)
        template = template.replace("{{title" + str(i+1) + "}}", title)

def printfont(ListUrls):
    global  template
    for i in range(0, len(ListUrls)):
        List = ListUrls[i]
        font = List.string
        template = template.replace("{{font" + str(i) + "}}", font)

def newspage():
    #for i in range(0.16):
        #global temp[i]
    ListUrls1 = content('\/Default.aspx\?tabid=35096&ctl=Detail&mid=65550&Id=[230602,239979].*')
    for i in range(0,len(ListUrls1)):
        List=ListUrls1[i]
        href=List.get('href')
        if href.startswith('http'):
            href=href
        else:
            href='http://en.math.shu.edu.cn/'+href
        res = request.urlopen(href)
        soup = BeautifulSoup(res, 'html.parser')
        #font_div = soup.find(attrs={"id": "dnn_ctr65550_ArtDetail_lblArticle"})
        #font_a = font_div.findAll('p')
        #if font_a=='None':
        font_div = soup.find(attrs={"id": "dnn_ctr65550_ArtDetail_zoom"})
        font_a = font_div.findAll('span')
        title = soup.find(attrs={"id": "dnn_ctr65550_ArtDetail_lblTitle"})
        for j in range(0,len(font_a)):
            font = font_a[j].decode_contents(formatter="html")
            temp[i] = temp[i].replace("{{font"+str(j)+"}}",font)
        for j in range (0,16):
            temp[i]=temp[i].replace("{{font"+str(j)+"}}",'')
        temp[i]=temp[i].replace("{{title}}",title.text)
        file = codecs.open(r'./docs/math/ensingle'+str(i)+'.html', 'w', encoding='utf-8')
        file.write(temp[i])
        file.close()

if __name__=='__main__':
    newspage()

    ListUrls1 = content('\/Default.aspx\?tabid=35096&ctl=Detail&mid=65550&Id=[230602,239979].*')
    printfont(ListUrls1)

    ListUrls2 = content('\/LinkClick.aspx\?link=.*')
    printadd(ListUrls2)

    #print(template)
    file = codecs.open(r'./docs/math/indexen.html', 'w', encoding='utf-8')
    file.write(template)
    file.close()