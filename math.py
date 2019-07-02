# -*- coding: utf-8 -*-
from urllib import  request
from bs4 import BeautifulSoup
import   os
import codecs

template='''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
   
    
	<title>上海大学数学系</title>
	
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
    <style type="text/css">
<!--
.STYLE1 {font-size:24px
	font-weight: bold;
	color: #FFFFFF;
}
.STYLE2 {font-size: 10px}
.STYLE3 {color: #F0F0F0}
-->
    </style>
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
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35826">
						<i class="fa fa-tags"></i>本系概况</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=36869">
						<i class="fa fa-tags"></i>
						<span>机构设置</span></a></li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37887">
						<i class="fa fa-tags"></i>师资队伍</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37894">
						<i class="fa fa-tags"></i>科学研究</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37903">
						<i class="fa fa-tags"></i>人才培养</a>
				</li>
				<li>
					<a href="www.math.shu.edu.cn/Default.aspx?tabid=37906">
						<i class="fa fa-tags"></i>国际交流</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=39411">
						<i class="fa fa-tags"></i>安全宣传</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37897">
						<i class="fa fa-tags"></i>联系我们</a>
				</li>
				<li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35743&ctl=login">
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
			<!-- Carousel -->
			<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
				
				<!-- Wrapper for slides -->
				<div class="carousel-inner">
					<div class="item active">
						<img src="images/1.jpg" alt="First slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<h2>上海大学 理学院 数学系</h2>
								<p class="STYLE1">Shanghai University Department of Mathematics</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img1}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit1}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img2}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit2}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img3}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit3}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img4}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit4}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img5}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit5}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img6}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit6}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img7}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit7}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img8}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit8}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img9}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text">
							<div class="col-md-12 text-center">
								<p class="badge">{{imgtit9}}</p>
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
										<h2>新闻快递</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2"><a href="{{link1}}">{{title1}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link2}}">{{title2}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link3}}">{{title3}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link4}}">{{title4}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link5}}">{{title5}}</a></p>
									<p align="left" class="STYLE2"><a href="{{link6}}">{{title6}}</a></p>
								</div>
							</div>
						</div>
					</article>
					<article  class="box-shadow">
						<div class="no-gutter">
							<div class="col-sm-6">
								<img src="images/8.jpg">
							</div>
							<div class="col-sm-6">
								<div class="art-content text-center">
									<div class="heading">
										<h2>学术会议</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2"><a href="{{link7}}">{{title7}}</p>
									<p align="left" class="STYLE2"><a href="{{link8}}">{{title8}}</p>
									<p align="left" class="STYLE2"><a href="{{link9}}">{{title9}}</p>
									<p align="left" class="STYLE2"><a href="{{link10}}">{{title10}}</p>
									<p align="left" class="STYLE2"><a href="{{link11}}">{{title11}}</p>
									<p align="left" class="STYLE2"><a href="{{link12}}">{{title12}}</p>
									<a class="btn btn-theme">更多...</a>
								</div>
							</div>
						</div>
					</article>
				</div>
				<div class="col-lg-6">
					<article  class="box-shadow">
					  <div class="no-gutter">
							<div class="col-sm-6 fix-right">
								<img src="images/6.jpg">
							</div>
							<div class="col-sm-6">
								<div class="art-content text-center">
									<div class="heading">
										<h2>学术报告</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2"><a href="{{link13}}">{{title13}}</p>
									<p align="left" class="STYLE2"><a href="{{link14}}">{{title14}}</p>
									<p align="left" class="STYLE2"><a href="{{link15}}">{{title15}}</p>
									<p align="left" class="STYLE2"><a href="{{link16}}">{{title16}}</p>
									<p align="left" class="STYLE2"><a href="{{link17}}">{{title17}}</p>
									<p align="left" class="STYLE2"><a href="{{link18}}">{{title18}}</p>
									<a class="btn btn-theme">更多...</a>
								</div>
							</div>
						    </div>
					</article>
					<article  class="box-shadow">
						<div class="no-gutter">
							<div class="col-sm-6">
								<img src="images/5.jpg">
							</div>
							<div class="col-sm-6">
								<div class="art-content text-center">
									<div class="heading">
										<h2>链接</h2>
										<hr class="line">
									</div>
									<p align="left" class="STYLE2">
									<a href="{{link19}}">{{title19}}  	<a href="{{link20}}">{{title20}}  <a href="{{link21}}">{{title21}}									</p>
									<p align="left" class="STYLE2">
									<a href="{{link22}}">{{title22}} 		<a href="{{link23}}">{{title23}}	    <a href="{{link24}}">{{title24}}									</p>
									<p align="left" class="STYLE2">
									<a href="{{link25}}">{{title25}}		<a href="{{link26}}">{{title26}}	   	<a href="{{link27}}">{{title27}}								</p>
									<p align="left" class="STYLE2">
									<a href="{{link28}}">{{title28}}	<a href="{{link29}}">{{title29}} <a href="{{link30}}">{{title30}}							</p>
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
</html>'''

def content(id):
    res = request.urlopen('http://www.math.shu.edu.cn/')
    soup = BeautifulSoup(res, "html.parser")
    new_div = soup.find(attrs={"id": id})
    new_a = new_div.findAll('a')
    return new_a

def getimg(id):
    res = request.urlopen('http://cmsarticle.shu.edu.cn/PicChage_157_mathen.aspx?cateId=7302&Domain=en.math.shu.edu.cn&Top=9')
    soup = BeautifulSoup(res, "html.parser")
    img_div = soup.find(attrs={"id":id})
    img_a = img_div.findAll('img')
    return img_a

def getimgtit(id):
    res = request.urlopen('http://cmsarticle.shu.edu.cn/PicChage_157_mathen.aspx?cateId=7302&Domain=en.math.shu.edu.cn&Top=9')
    soup = BeautifulSoup(res,"html.parser")
    img_div = soup.find(attrs={"id": id})
    img_a = img_div.findAll('b')
    return img_a

def printadd(new_a,start):
    global template
    for i in range(0,len(new_a)):
        new=new_a[i]
        title=new.string
        if new.get('href').startswith('http'):
            href=new.get('href')
        else:
            href='http://www.math.shu.edu.cn' + new.get('href')
        template=template.replace("{{link"+str(start+i)+"}}",href)
        template=template.replace("{{title"+str(start+i)+"}}",title)

def printimg(img_a,imgtit):
    global template
    for i in range(0, len(img_a)):
        img = img_a[i]
        imgtitle = imgtit[i]
        src = img.get('src')
        template = template.replace("{{img" + str(i+1) + "}}", src)
        template = template.replace("{{imgtit" + str(i + 1) + "}}", imgtitle.string)

def getlink(id):
    res = request.urlopen('http://www.math.shu.edu.cn')
    soup = BeautifulSoup(res, "html.parser")
    link_div = soup.find(attrs={"id": id})
    link_a = img_div.findAll('td')
    print(link_a.get('src'))
    #return link_a

if __name__ == '__main__':

    new_a1 = content('dnn_ctr67554_ModuleContent')
    printadd(new_a1,1)

    new_a2 = content('dnn_ctr67559_ModuleContent')
    printadd(new_a2,7)

    new_a3 = content('dnn_ctr67556_ModuleContent')
    printadd(new_a3,13)

    new_a4 = content('dnn_ctr67562_ModuleContent')
    printadd(new_a4,19)

    img_a = getimg('games')
    imgtit = getimgtit('games')
    printimg(img_a,imgtit)

    print(template)
    file = codecs.open(r'./docs/index.html','w',encoding='utf-8')
    file.write(template)
    file.close()
    os.system(r'git commit -am "auto update"')
    os.system(r'git push')


