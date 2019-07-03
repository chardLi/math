# -*- coding: utf-8 -*-
from urllib import  request
from bs4 import BeautifulSoup
import   os
import codecs

temp = []
for i in range(0, 18):
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

template='''
<!DOCTYPE html>
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
    </style>
</head>

<body style="background-color:#222">
   <!--header start-->
	<header class="header">
		<div class="sidebar-toggle-box">
			<div class="fa fa-bars tooltips" data-placement="right"></div>
		</div>
		<!--logo start-->
		<a href="http://www.shu.edu.cn/" class="logo"><strong>上海大学</strong></a>
		<!--logo end-->
		
		<div class="top-menu">
			<ul class="nav pull-right top-menu">
				<li><a class="social" href="http://www.math.shu.edu.cn/Default.aspx?tabid=35743&ctl=login">登录</a></li>
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
                    <a href="#"><i class="fa fa-tags"></i>首页</a>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>本系概况<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35826">历史沿革</a>
                        </li>
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35827">师资力量</a>
                        </li>
						<li>
							<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35828">人才培养</a>
						</li>
                    </ul>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>机构设置<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=36869">系党政机构</a>
                        </li>
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37891">系学术委员会</a>
                        </li>
						  <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37892">系教学指导委员会</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37893">系教学与科研机构</a>
                        </li>
                    </ul>
                 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>师资队伍<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38059">领军人物</a>
                        </li>
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37887">教授</a>
                        </li>
						  <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37888">副教授</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37889">讲师</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38061">博士后</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38060">荣誉/兼职教授</a>
                        </li>
					</ul>
				 </li>
				 <li>
                    <a href="#"><i class="fa fa-tags"></i>科学研究<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37898">研究方向</a>
                        </li>
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37899">科研项目</a>
                        </li>
						  <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37900">学术论文</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37901">科研机构</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37902">科技奖励</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38064">学术著作</a>
                        </li>
						<li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38069">学术期刊</a>
                        </li>
                    </ul>
                 </li>
				  <li>
                    <a href="#"><i class="fa fa-tags"></i>人才培养<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37903">就业介绍</a>
                        </li>
                        <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37904">培养方案</a>
                        </li>
						  <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37905">学科竞赛</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38062">实践工作站</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37903">科技奖励</a>
                        </li>
						 <li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38080">研究生教育</a>
                        </li>
						<li>
                            <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=38083">本科生教育</a>
                        </li>
                    </ul>
                 </li>
				 		<li>
                    <a href="#"><i class="fa fa-tags"></i>国际交流<span
                                class="fa arrow"></span></a>
                    <ul class="nav nav-second-level">
                        <li>
                            <a href="www.math.shu.edu.cn/Default.aspx?tabid=37906">国际合作</a>
                        </li>
                        <li>
                            <a href="www.math.shu.edu.cn/Default.aspx?tabid=37907">国际会议</a>
                        </li>
                    </ul>
                 </li>
				 <li>
                    <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=39411"><i class="fa fa-tags"></i>安全宣传</a>
                 </li>
				 <li>
                    <a href="http://www.math.shu.edu.cn/Default.aspx?tabid=37897"><i class="fa fa-tags"></i>联系我们</a>
                 </li>
				 <li>
					<a href="http://www.math.shu.edu.cn/Default.aspx?tabid=35743&ctl=login">
						<i class="fa fa-tags"></i>登录</a>
				</li>
				 <li>
                    <a href="indexen.html"><i class="fa fa-tags"></i>English</a>
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
								<h2>上海大学 理学院 数学系</h2>
								<p class="STYLE1">Shanghai University Department of Mathematics</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img1}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit1}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img2}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit2}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img3}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit3}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img4}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit4}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img5}}" alt="Third slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit5}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img6}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit6}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img7}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit7}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img8}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit8}}</p>
								<br>
							</div>
						</div><!-- /header-text -->
					</div>
					<div class="item">
						<img src="{{img9}}" alt="Second slide">
						<!-- Static Header -->
						<div class="header-text1">
							<div class="col-md-12 text-center">
								<p class="badge" style="font-size:20px">{{imgtit9}}</p>
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
									<p align="left" class="STYLE2"><a href="single0.html">{{font0}}</a></p>
									<p align="left" class="STYLE2"><a href="single1.html">{{font1}}</a></p>
									<p align="left" class="STYLE2"><a href="single2.html">{{font2}}</a></p>
									<p align="left" class="STYLE2"><a href="single3.html">{{font3}}</a></p>
									<p align="left" class="STYLE2"><a href="single4.html">{{font4}}</a></p>
									<p align="left" class="STYLE2"><a href="single5.html">{{font5}}</a></p>
									<a class="btn btn-theme" href="http://www.math.shu.edu.cn/Default.aspx?tabid=37909">更多...</a>
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
									<p align="left" class="STYLE2"><a href="single6.html">{{font6}}</p>
									<p align="left" class="STYLE2"><a href="single7.html">{{font7}}</p>
									<p align="left" class="STYLE2"><a href="single8.html">{{font8}}</p>
									<p align="left" class="STYLE2"><a href="single9.html">{{font9}}</p>
									<p align="left" class="STYLE2"><a href="single10.html">{{font10}}</p>
									<p align="left" class="STYLE2"><a href="single11.html">{{font11}}</p>
									<a class="btn btn-theme" href="http://www.math.shu.edu.cn/Default.aspx?tabid=37911">更多...</a>
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
									<p align="left" class="STYLE2"><a href="single12.html">{{font12}}</p>
									<p align="left" class="STYLE2"><a href="single13.html">{{font13}}</p>
									<p align="left" class="STYLE2"><a href="single14.html">{{font14}}</p>
									<p align="left" class="STYLE2"><a href="single15.html">{{font15}}</p>
									<p align="left" class="STYLE2"><a href="single16.html">{{font16}}</p>
									<p align="left" class="STYLE2"><a href="single17.html">{{font17}}</p>
									<a class="btn btn-theme" href="http://www.math.shu.edu.cn/Default.aspx?tabid=37910">更多...</a>
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
									<a href="{{link0}}">{{title0}}  	<a href="{{link1}}">{{title1}}  <a href="{{link2}}">{{title}}									</p>
									<p align="left" class="STYLE2">
									<a href="{{link3}}">{{title3}} 		<a href="{{link4}}">{{title4}}	    <a href="{{link5}}">{{title5}}									</p>
									<p align="left" class="STYLE2">
									<a href="{{link6}}">{{title6}}		<a href="{{link7}}">{{title7}}	   	<a href="{{link8}}">{{title8}}								</p>
									<p align="left" class="STYLE2">
									<a href="{{link9}}">{{title9}}	<a href="{{link10}}">{{title10}} <a href="{{link11}}">{{title11}}							</p>
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

def printadd(new_a):
    global template
    for i in range(0,len(new_a)):
        new=new_a[i]
        title=new.string
        if new.get('href').startswith('http'):
            href=new.get('href')
        else:
            href='http://www.math.shu.edu.cn' + new.get('href')
        template=template.replace("{{link"+str(i)+"}}",href)
        template=template.replace("{{title"+str(i)+"}}",title)

def printimg(img_a,imgtit):
    global template
    for i in range(0, len(img_a)):
        img = img_a[i]
        imgtitle = imgtit[i]
        src = img.get('src')
        template = template.replace("{{img" + str(i+1) + "}}", src)
        template = template.replace("{{imgtit" + str(i + 1) + "}}", imgtitle.string)

def printfont(new_a,start):
    global  template
    for i in range(0, len(new_a)):
        new = new_a[i]
        font = new.string
        template = template.replace("{{font" + str(start+i) + "}}", font)

def newspage(id,newid,newtit,start):
    #for i in range(0.16):
        #global temp[i]
    ListUrls1 = content(id)
    for i in range(start,len(ListUrls1)+start):
        List=ListUrls1[i-start]
        href=List.get('href')
        if href.startswith('http'):
            href=href
        else:
            href='http://www.math.shu.edu.cn/'+href
        res = request.urlopen(href)
        soup = BeautifulSoup(res, 'html.parser')
        #font_div = soup.find(attrs={"id": "dnn_ctr65550_ArtDetail_lblArticle"})
        #font_a = font_div.findAll('p')
        #if font_a=='None':
        font_div = soup.find(attrs={"id": newid})
        font_a = font_div.findAll('span')
        title = soup.find(attrs={"id": newtit})
        for j in range(0,len(font_a)):
            font = font_a[j].decode_contents(formatter="html")
            temp[i] = temp[i].replace("{{font"+str(j)+"}}",font)
        for j in range (0,16):
            temp[i]=temp[i].replace("{{font"+str(j)+"}}",'')
        temp[i]=temp[i].replace("{{title}}",title.text)
        file = codecs.open(r'./docs/math/single'+str(i)+'.html', 'w', encoding='utf-8')
        file.write(temp[i])
        file.close()

if __name__ == '__main__':

    new_a1 = content('dnn_ctr67554_ModuleContent')
    printfont(new_a1, 0)
    newspage('dnn_ctr67554_ModuleContent','dnn_ctr67554_ArtDetail_zoom','dnn_ctr67554_ArtDetail_lblTitle',0)

    new_a2 = content('dnn_ctr67559_ModuleContent')
    printfont(new_a2, 6)
    #newspage('dnn_ctr67559_ModuleContent','dnn_ctr64531_ArtDetail_zoom','dnn_ctr67556_ArtDetail_lblTitle',6)

    new_a3 = content('dnn_ctr67556_ModuleContent')
    printfont(new_a3, 12)
    newspage('dnn_ctr67556_ModuleContent','dnn_ctr67556_ArtDetail_zoom','dnn_ctr67556_ArtDetail_lblTitle',12)

    new_a4 = content('dnn_ctr67562_ModuleContent')
    printadd(new_a4)

    img_a = getimg('games')
    imgtit = getimgtit('games')
    printimg(img_a, imgtit)

    print(template)
    file = codecs.open(r'./docs/math/index.html', 'w', encoding='utf-8')
    file.write(template)
    file.close()
    os.system(r'git commit -am "auto update"')
    os.system(r'git push')


