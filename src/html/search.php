<!DOCTYPE html>
<html lang="en">
<head>
    <title>Search Results</title>
    <meta charset="utf-8">
    <meta name="format-detection" content="telephone=no"/>
    <link rel="icon" href="images/favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="css/grid.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/jquery.fancybox.css"/>
    <link rel="stylesheet" href="css/camera.css"/>
    <link rel="stylesheet" href="css/contact-form.css"/>

    <script src="js/jquery.js"></script>
    <script src="js/jquery-migrate-1.2.1.js"></script>
    <script src='js/raphael/raphael.js'></script>
    <script src='search/search.js'></script>

    <!--[if lt IE 9]>
    <html class="lt-ie9">
    <div style=' clear: both; text-align:center; position: relative;'>
        <a href="http://windows.microsoft.com/en-US/internet-explorer/..">
            <img src="images/ie8-panel/warning_bar_0000_us.jpg" border="0" height="42" width="820"
                 alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today."/>
        </a>
    </div>
    <script src="js/html5shiv.js"></script>
    <![endif]-->

    <script src='js/device.min.js'></script>
</head>

<body>
<div class="page">
    <!--========================================================
                              HEADER
    =========================================================-->
    <header id="header" class="header">
        <div id="stuck_container" class="stuck_container">
            <div class="container">
                <nav class="nav">
                    <ul class="sf-menu">
                        <li>
                            <a href="index.html#about">About Us</a>
                        </li>
                        <li>
                            <a href="index.html#team">Our Team</a>
                            <ul>
                                <li>
                                    <a href="#">Quisque nulla</a>
                                </li>
                                <li>
                                    <a href="#">Vestibulum libero</a>
                                    <ul>
                                        <li>
                                            <a href="#">Lorem</a>
                                        </li>
                                        <li>
                                            <a href="#">Dolor</a>
                                        </li>
                                        <li>
                                            <a href="#">Sit amet</a>
                                        </li>
                                    </ul>
                                </li>
                                <li>
                                    <a href="#">Vivamus eget nibh</a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="index.html#services">Service Area</a>
                        </li>
                        <li>
                            <a href="index.html#products">Our Products</a>
                        </li>
                        <li>
                            <a href="index.html#contacts">Contacts</a>
                        </li>
                    </ul>
                </nav>
                <a class="search-form-toggle" href="#"></a>
            </div>
            <div class="search-form">
                <div class="container">
                    <form id="search" action="search.php" method="GET"
                          accept-charset="utf-8">
                        <label class="input">
                            <input type="text" name="s" placeholder="Type your search term here..."/>
                        </label>
                        <button type="submit" class="fa fa-search"></button>
                    </form>
                </div>
            </div>
        </div>

        <div class="header_panel">
            <div class="container">
                <div class="brand">
                    <h1 class="brand_name">
                        <a href="./"><span class="primary">Food</span>Broker</a>
                    </h1>

                    <p class="brand_slogan">
                        <span class="primary">Nationally respected</span>&nbsp;&nbsp;&nbsp;&nbsp;food expert
                    </p>
                </div>

                <ul class="social-list">
                    <li>
                        <a class="fa fa-google-plus" href="#"></a>
                    </li>
                    <li>
                        <a class="fa fa-twitter" href="#"></a>
                    </li>
                    <li>
                        <a class="fa fa-facebook" href="#"></a>
                    </li>
                    <li>
                        <a class="fa fa-pinterest" href="#"></a>
                    </li>
                    <li>
                        <a class="fa fa-linkedin" href="#"></a>
                    </li>
                </ul>
                <ul class="inline-list">
                    <li>
                        <a href="#">login</a>
                    </li>
                    <li>
                        <a href="#">help</a>
                    </li>
                    <li>
                        <a href="#">newsletter signup</a>
                    </li>
                </ul>
            </div>
        </div>

    </header>
    <!--========================================================
                              CONTENT
    =========================================================-->

    <section id="content" class="content">
        <div class="container well center">
            <div class="row">
                <div class="grid_10 preffix_1">
                    <h3 class="primary">Search Results</h3>

                    <div class="row">
                        <div class="grid_10">
                            <div id="search-results"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!--========================================================
                              FOOTER
    =========================================================-->
    <footer id="footer" class="footer  footer__ins1">
        <div class="container">
            <div class="copyright">
                FOOD BROKER.
                © <span id="copyright-year"></span>
                <a href="index-1.html">Privacy policy</a>
            </div>
        </div>
    </footer>
</div>

<script src="js/script.js"></script>

<!--coded by Diversant-->
</body>
</html>