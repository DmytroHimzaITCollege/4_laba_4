{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'<!DOCTYPE html>'\n",
      "b'<html lang=\"en\">'\n",
      "b''\n",
      "b'<head>'\n",
      "b'    <meta charset=\"UTF-8\">'\n",
      "b'    <title>httpbin.org</title>'\n",
      "b'    <link href=\"https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700\"'\n",
      "b'        rel=\"stylesheet\">'\n",
      "b'    <link rel=\"stylesheet\" type=\"text/css\" href=\"/flasgger_static/swagger-ui.css\">'\n",
      "b'    <link rel=\"icon\" type=\"image/png\" href=\"/static/favicon.ico\" sizes=\"64x64 32x32 16x16\" />'\n",
      "b'    <style>'\n",
      "b'        html {'\n",
      "b'            box-sizing: border-box;'\n",
      "b'            overflow: -moz-scrollbars-vertical;'\n",
      "b'            overflow-y: scroll;'\n",
      "b'        }'\n",
      "b''\n",
      "b'        *,'\n",
      "b'        *:before,'\n",
      "b'        *:after {'\n",
      "b'            box-sizing: inherit;'\n",
      "b'        }'\n",
      "b''\n",
      "b'        body {'\n",
      "b'            margin: 0;'\n",
      "b'            background: #fafafa;'\n",
      "b'        }'\n",
      "b'    </style>'\n",
      "b'</head>'\n",
      "b''\n",
      "b'<body>'\n",
      "b'    <a href=\"https://github.com/requests/httpbin\" class=\"github-corner\" aria-label=\"View source on Github\">'\n",
      "b'        <svg width=\"80\" height=\"80\" viewBox=\"0 0 250 250\" style=\"fill:#151513; color:#fff; position: absolute; top: 0; border: 0; right: 0;\"'\n",
      "b'            aria-hidden=\"true\">'\n",
      "b'            <path d=\"M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z\"></path>'\n",
      "b'            <path d=\"M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2\"'\n",
      "b'                fill=\"currentColor\" style=\"transform-origin: 130px 106px;\" class=\"octo-arm\"></path>'\n",
      "b'            <path d=\"M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z\"'\n",
      "b'                fill=\"currentColor\" class=\"octo-body\"></path>'\n",
      "b'        </svg>'\n",
      "b'    </a>'\n",
      "b'    <svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" style=\"position:absolute;width:0;height:0\">'\n",
      "b'        <defs>'\n",
      "b'            <symbol viewBox=\"0 0 20 20\" id=\"unlocked\">'\n",
      "b'                <path d=\"M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V6h2v-.801C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8z\"></path>'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 20 20\" id=\"locked\">'\n",
      "b'                <path d=\"M15.8 8H14V5.6C14 2.703 12.665 1 10 1 7.334 1 6 2.703 6 5.6V8H4c-.553 0-1 .646-1 1.199V17c0 .549.428 1.139.951 1.307l1.197.387C5.672 18.861 6.55 19 7.1 19h5.8c.549 0 1.428-.139 1.951-.307l1.196-.387c.524-.167.953-.757.953-1.306V9.199C17 8.646 16.352 8 15.8 8zM12 8H8V5.199C8 3.754 8.797 3 10 3c1.203 0 2 .754 2 2.199V8z\"'\n",
      "b'                />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 20 20\" id=\"close\">'\n",
      "b'                <path d=\"M14.348 14.849c-.469.469-1.229.469-1.697 0L10 11.819l-2.651 3.029c-.469.469-1.229.469-1.697 0-.469-.469-.469-1.229 0-1.697l2.758-3.15-2.759-3.152c-.469-.469-.469-1.228 0-1.697.469-.469 1.228-.469 1.697 0L10 8.183l2.651-3.031c.469-.469 1.228-.469 1.697 0 .469.469.469 1.229 0 1.697l-2.758 3.152 2.758 3.15c.469.469.469 1.229 0 1.698z\"'\n",
      "b'                />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 20 20\" id=\"large-arrow\">'\n",
      "b'                <path d=\"M13.25 10L6.109 2.58c-.268-.27-.268-.707 0-.979.268-.27.701-.27.969 0l7.83 7.908c.268.271.268.709 0 .979l-7.83 7.908c-.268.271-.701.27-.969 0-.268-.269-.268-.707 0-.979L13.25 10z\"'\n",
      "b'                />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 20 20\" id=\"large-arrow-down\">'\n",
      "b'                <path d=\"M17.418 6.109c.272-.268.709-.268.979 0s.271.701 0 .969l-7.908 7.83c-.27.268-.707.268-.979 0l-7.908-7.83c-.27-.268-.27-.701 0-.969.271-.268.709-.268.979 0L10 13.25l7.418-7.141z\"'\n",
      "b'                />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 24 24\" id=\"jump-to\">'\n",
      "b'                <path d=\"M19 7v4H5.83l3.58-3.59L8 6l-6 6 6 6 1.41-1.41L5.83 13H21V7z\" />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'            <symbol viewBox=\"0 0 24 24\" id=\"expand\">'\n",
      "b'                <path d=\"M10 18h4v-2h-4v2zM3 6v2h18V6H3zm3 7h12v-2H6v2z\" />'\n",
      "b'            </symbol>'\n",
      "b''\n",
      "b'        </defs>'\n",
      "b'    </svg>'\n",
      "b''\n",
      "b''\n",
      "b'    <div id=\"swagger-ui\">'\n",
      "b'        <div data-reactroot=\"\" class=\"swagger-ui\">'\n",
      "b'            <div>'\n",
      "b'                <div class=\"information-container wrapper\">'\n",
      "b'                    <section class=\"block col-12\">'\n",
      "b'                        <div class=\"info\">'\n",
      "b'                            <hgroup class=\"main\">'\n",
      "b'                                <h2 class=\"title\">httpbin.org'\n",
      "b'                                    <small>'\n",
      "b'                                        <pre class=\"version\">0.9.2</pre>'\n",
      "b'                                    </small>'\n",
      "b'                                </h2>'\n",
      "b'                                <pre class=\"base-url\">[ Base URL: httpbin.org/ ]</pre>'\n",
      "b'                            </hgroup>'\n",
      "b'                            <div class=\"description\">'\n",
      "b'                                <div class=\"markdown\">'\n",
      "b'                                    <p>A simple HTTP Request &amp; Response Service.'\n",
      "b'                                        <br>'\n",
      "b'                                        <br>'\n",
      "b'                                        <b>Run locally: </b>'\n",
      "b'                                        <code>$ docker run -p 80:80 kennethreitz/httpbin</code>'\n",
      "b'                                    </p>'\n",
      "b'                                </div>'\n",
      "b'                            </div>'\n",
      "b'                            <div>'\n",
      "b'                                <div>'\n",
      "b'                                    <a href=\"https://kennethreitz.org\" target=\"_blank\">the developer - Website</a>'\n",
      "b'                                </div>'\n",
      "b'                                <a href=\"mailto:me@kennethreitz.org\">Send email to the developer</a>'\n",
      "b'                            </div>'\n",
      "b'                        </div>'\n",
      "b'                        <!-- ADDS THE LOADER SPINNER -->'\n",
      "b'                        <div class=\"loading-container\">'\n",
      "b'                            <div class=\"loading\"></div>'\n",
      "b'                        </div>'\n",
      "b''\n",
      "b'                    </section>'\n",
      "b'                </div>'\n",
      "b'            </div>'\n",
      "b'        </div>'\n",
      "b'    </div>'\n",
      "b''\n",
      "b''\n",
      "b\"    <div class='swagger-ui'>\"\n",
      "b'        <div class=\"wrapper\">'\n",
      "b'            <section class=\"clear\">'\n",
      "b'                <span style=\"float: right;\">'\n",
      "b'                    [Powered by'\n",
      "b'                    <a target=\"_blank\" href=\"https://github.com/rochacbruno/flasgger\">Flasgger</a>]'\n",
      "b'                    <br>'\n",
      "b'                </span>'\n",
      "b'            </section>'\n",
      "b'        </div>'\n",
      "b'    </div>'\n",
      "b''\n",
      "b''\n",
      "b''\n",
      "b'    <script src=\"/flasgger_static/swagger-ui-bundle.js\"> </script>'\n",
      "b'    <script src=\"/flasgger_static/swagger-ui-standalone-preset.js\"> </script>'\n",
      "b\"    <script src='/flasgger_static/lib/jquery.min.js' type='text/javascript'></script>\"\n",
      "b'    <script>'\n",
      "b''\n",
      "b'        window.onload = function () {'\n",
      "b'            '\n",
      "b''\n",
      "b'            fetch(\"/spec.json\")'\n",
      "b'                .then(function (response) {'\n",
      "b'                    response.json()'\n",
      "b'                        .then(function (json) {'\n",
      "b'                            var current_protocol = window.location.protocol.slice(0, -1);'\n",
      "b'                            if (json.schemes[0] != current_protocol) {'\n",
      "b'                                // Switches scheme to the current in use'\n",
      "b'                                var other_protocol = json.schemes[0];'\n",
      "b'                                json.schemes[0] = current_protocol;'\n",
      "b'                                json.schemes[1] = other_protocol;'\n",
      "b''\n",
      "b'                            }'\n",
      "b'                            json.host = window.location.host;  // sets the current host'\n",
      "b''\n",
      "b'                            const ui = SwaggerUIBundle({'\n",
      "b'                                spec: json,'\n",
      "b'                                validatorUrl: null,'\n",
      "b\"                                dom_id: '#swagger-ui',\"\n",
      "b'                                deepLinking: true,'\n",
      "b'                                jsonEditor: true,'\n",
      "b'                                docExpansion: \"none\",'\n",
      "b'                                apisSorter: \"alpha\",'\n",
      "b'                                //operationsSorter: \"alpha\",'\n",
      "b'                                presets: ['\n",
      "b'                                    SwaggerUIBundle.presets.apis,'\n",
      "b'                                    // yay ES6 modules \\xe2\\x86\\x98'\n",
      "b'                                    Array.isArray(SwaggerUIStandalonePreset) ? SwaggerUIStandalonePreset : SwaggerUIStandalonePreset.default'\n",
      "b'                                ],'\n",
      "b'                                plugins: ['\n",
      "b'                                    SwaggerUIBundle.plugins.DownloadUrl'\n",
      "b'                                ],'\n",
      "b'            '\n",
      "b'            // layout: \"StandaloneLayout\"  // uncomment to enable the green top header'\n",
      "b'        })'\n",
      "b''\n",
      "b'        window.ui = ui'\n",
      "b''\n",
      "b'        // uncomment to rename the top brand if layout is enabled'\n",
      "b'        // $(\".topbar-wrapper .link span\").replaceWith(\"<span>httpbin</span>\");'\n",
      "b'        })'\n",
      "b'    })'\n",
      "b'}'\n",
      "b\"    </script>  <div class='swagger-ui'>\"\n",
      "b'    <div class=\"wrapper\">'\n",
      "b'        <section class=\"block col-12 block-desktop col-12-desktop\">'\n",
      "b'            <div>'\n",
      "b''\n",
      "b'                <h2>Other Utilities</h2>'\n",
      "b''\n",
      "b'                <ul>'\n",
      "b'                    <li>'\n",
      "b'                        <a href=\"/forms/post\">HTML form</a> that posts to /post /forms/post</li>'\n",
      "b'                </ul>'\n",
      "b''\n",
      "b'                <br />'\n",
      "b'                <br />'\n",
      "b'            </div>'\n",
      "b'        </section>'\n",
      "b'    </div>'\n",
      "b'</div>'\n",
      "b'</body>'\n",
      "b''\n",
      "b'</html>'\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "response = requests.get('https://httpbin.org/')\n",
    "for line in response.iter_lines():\n",
    "    print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'HELLO'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [3], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mos\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m os\u001b[39m.\u001b[39;49menviron[\u001b[39m'\u001b[39;49m\u001b[39mHELLO\u001b[39;49m\u001b[39m'\u001b[39;49m]\n",
      "File \u001b[1;32m<frozen os>:678\u001b[0m, in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'HELLO'"
     ]
    }
   ],
   "source": [
    "import os\n",
    "os.environ['HELLO']"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.11.0 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "f20ab87d6a3ff6ba42d2ef397e4f998400337c529080cfa5d542bf12e78eea55"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
