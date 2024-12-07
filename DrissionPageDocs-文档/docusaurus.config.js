// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
    title: 'DrissionPage官网',
    tagline: '简洁而强大',
    favicon: 'img/DrissionPage.ico',
    scripts: [
        // 对象格式。
        {
            src: 'https://cdn.wwads.cn/js/makemoney.js',
            async: true,
        },
        // {
        //     src: 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2356291831611012',
        //     async: true,
        //     crossorigin: "anonymous"
        // },
    ],
    // Set the production url of your site here
    url: 'https://www.drissionpage.cn',
    // Set the /<baseUrl>/ pathname under which your site is served
    // For GitHub pages deployment, it is often '/<projectName>/'
    baseUrl: '/',

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: 'Drission', // Usually your GitHub org/user name.
    projectName: 'DrissionPage', // Usually your repo name.

    onBrokenLinks: 'throw',
    onBrokenMarkdownLinks: 'warn',

    // Even if you don't use internationalization, you can use this field to set
    // useful metadata like html lang. For example, if your site is Chinese, you
    // may want to replace "en" with "zh-Hans".
    i18n: {
        defaultLocale: 'zh-cn',
        locales: ['zh-cn'],
    },

    presets: [
        [
            'classic',
//      '@docusaurus/preset-classic',
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
                docs: {
                    routeBasePath: '/',
                    sidebarPath: './sidebars.js',

                    // Please change this to your repo.
                    // Remove this to remove the "edit this page" links.
//          editUrl:
//            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
                },
//        blog: {
//          showReadingTime: true,
//          // Please change this to your repo.
//          // Remove this to remove the "edit this page" links.
//          editUrl:
//            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
//        },
                theme: {
                    customCss: './src/css/custom.css',
                },
            }),
        ],
    ],

    themeConfig:
//    require.resolve("@easyops-cn/docusaurus-search-local"),
    /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
        ({
            // Replace with your project's social card
            colorMode: {defaultMode: 'dark'},
            image: 'img/docusaurus-social-card.jpg',
            navbar: {
                title: 'DrissionPage',
                logo: {
                    alt: 'DrissionPage',
                    src: 'img/color_logo.png',
                },
                items: [
//          {type: 'doc', docId: 'welcome', position: 'left', label: '欢迎'},
                    {type: 'docSidebar', sidebarId: 'featuresSidebar', position: 'left', label: '🔥特性介绍'},
                    {type: 'docSidebar', sidebarId: 'startSidebar', position: 'left', label: '入门指南'},
                    {type: 'docSidebar', sidebarId: 'usageSidebar', position: 'left', label: '使用文档'},
                    {type: 'docSidebar', sidebarId: 'demoSidebar', position: 'left', label: '实用教程'},
                    {type: 'docSidebar', sidebarId: 'versionsSidebar', position: 'left', label: '开发进度'},
                    // {type: 'doc', docId: 'ecotope', position: 'left', label: '软件生态'},
                    {type: 'doc', docId: 'support', position: 'left', label: '支持作者'},
//          {to: '/blog', label: 'Blog', position: 'left'},
                    {
                        type: 'dropdown',
                        label: '更多作品',
                        position: 'right',
                        items: [
                            {
                                label: 'DataRecorder',
                                href: 'https://drissionpage.cn/DataRecorderDocs',
                            },
                            {
                                label: 'DownloadKit',
                                href: 'https://drissionpage.cn/DownloadKitDocs',
                            },
                            {
                                label: 'MixPage',
                                href: 'https://drissionpage.cn/MixPageDocs',
                            },
                            {
                                label: '3.2版文档',
                                href: 'https://drissionpage.cn/DP32Docs',
                            },
                            {
                                label: '4.0版文档',
                                href: 'https://drissionpage.cn/DP40Docs',
                            },
                        ],
                    },
                    {
                        type: 'dropdown',
                        label: '项目地址',
                        position: 'right',
                        items: [
                            {
                                label: 'Gitee',
                                href: 'https://gitee.com/g1879/DrissionPage',
                            },
                            {
                                label: 'GitHub',
                                href: 'https://github.com/g1879/DrissionPage',
                            },
                        ]
                    },
                    {type: 'search', position: 'right',},
                ],
            },
            footer: {
                style: 'dark',
                links: [
                    {
                        title: '作者',
                        items: [
                            {
                                label: 'g1879',
                                href: 'https://gitee.com/g1879',
                            },
                        ],
                    },
                    {
                        title: '交流',
                        items: [
                            {
                                label: '联系邮箱：g1879@qq.com',
                                href: '#',
                            },
                            {
                                label: 'QQ群：636361957',
                                href: '#',
                            },
                        ],
                    },
                    {
                        title: '旧版地址',
                        items: [
                            {
                                label: '4.0版文档',
                                href: 'https://DrissionPage.cn/dp40docs/',
                            },
                            {
                                label: '3.2版文档',
                                href: 'https://DrissionPage.cn/dp32docs/',
                            },
                            {
                                label: 'MixPage',
                                href: 'https://DrissionPage.cn/mixpagedocs',
                            },
                        ],
                    },
                ],
                copyright: `<br/><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">本文档禁止商用 <a property="dct:title" rel="cc:attributionURL" href="https://drissionpage.cn">DrissionPageDocs</a> by <span property="cc:attributionName">g1879</span> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC 4.0</a>
<svg style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" id="Layer_1" x="0px" y="0px" width="22px" height="22px" viewBox="5.5 -3.5 64 64" enable-background="new 5.5 -3.5 64 64" xml:space="preserve">
<g>
\t<circle fill="#FFFFFF" cx="37.785" cy="28.501" r="28.836"/>
\t<path d="M37.441-3.5c8.951,0,16.572,3.125,22.857,9.372c3.008,3.009,5.295,6.448,6.857,10.314   c1.561,3.867,2.344,7.971,2.344,12.314c0,4.381-0.773,8.486-2.314,12.313c-1.543,3.828-3.82,7.21-6.828,10.143   c-3.123,3.085-6.666,5.448-10.629,7.086c-3.961,1.638-8.057,2.457-12.285,2.457s-8.276-0.808-12.143-2.429   c-3.866-1.618-7.333-3.961-10.4-7.027c-3.067-3.066-5.4-6.524-7-10.372S5.5,32.767,5.5,28.5c0-4.229,0.809-8.295,2.428-12.2   c1.619-3.905,3.972-7.4,7.057-10.486C21.08-0.394,28.565-3.5,37.441-3.5z M37.557,2.272c-7.314,0-13.467,2.553-18.458,7.657   c-2.515,2.553-4.448,5.419-5.8,8.6c-1.354,3.181-2.029,6.505-2.029,9.972c0,3.429,0.675,6.734,2.029,9.913   c1.353,3.183,3.285,6.021,5.8,8.516c2.514,2.496,5.351,4.399,8.515,5.715c3.161,1.314,6.476,1.971,9.943,1.971   c3.428,0,6.75-0.665,9.973-1.999c3.219-1.335,6.121-3.257,8.713-5.771c4.99-4.876,7.484-10.99,7.484-18.344   c0-3.543-0.648-6.895-1.943-10.057c-1.293-3.162-3.18-5.98-5.654-8.458C50.984,4.844,44.795,2.272,37.557,2.272z M37.156,23.187   l-4.287,2.229c-0.458-0.951-1.019-1.619-1.685-2c-0.667-0.38-1.286-0.571-1.858-0.571c-2.856,0-4.286,1.885-4.286,5.657   c0,1.714,0.362,3.084,1.085,4.113c0.724,1.029,1.791,1.544,3.201,1.544c1.867,0,3.181-0.915,3.944-2.743l3.942,2   c-0.838,1.563-2,2.791-3.486,3.686c-1.484,0.896-3.123,1.343-4.914,1.343c-2.857,0-5.163-0.875-6.915-2.629   c-1.752-1.752-2.628-4.19-2.628-7.313c0-3.048,0.886-5.466,2.657-7.257c1.771-1.79,4.009-2.686,6.715-2.686   C32.604,18.558,35.441,20.101,37.156,23.187z M55.613,23.187l-4.229,2.229c-0.457-0.951-1.02-1.619-1.686-2   c-0.668-0.38-1.307-0.571-1.914-0.571c-2.857,0-4.287,1.885-4.287,5.657c0,1.714,0.363,3.084,1.086,4.113   c0.723,1.029,1.789,1.544,3.201,1.544c1.865,0,3.18-0.915,3.941-2.743l4,2c-0.875,1.563-2.057,2.791-3.541,3.686   c-1.486,0.896-3.105,1.343-4.857,1.343c-2.896,0-5.209-0.875-6.941-2.629c-1.736-1.752-2.602-4.19-2.602-7.313   c0-3.048,0.885-5.466,2.658-7.257c1.77-1.79,4.008-2.686,6.713-2.686C51.117,18.558,53.938,20.101,55.613,23.187z"/>
</g>
</svg><svg style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" id="Layer_1" x="0px" y="0px" width="22px" height="22px" viewBox="5.5 -3.5 64 64" enable-background="new 5.5 -3.5 64 64" xml:space="preserve">
<g>
\t<circle fill="#FFFFFF" cx="37.637" cy="28.806" r="28.276"/>
\t<g>
\t\t<path d="M37.443-3.5c8.988,0,16.57,3.085,22.742,9.257C66.393,11.967,69.5,19.548,69.5,28.5c0,8.991-3.049,16.476-9.145,22.456    C53.879,57.319,46.242,60.5,37.443,60.5c-8.649,0-16.153-3.144-22.514-9.43C8.644,44.784,5.5,37.262,5.5,28.5    c0-8.761,3.144-16.342,9.429-22.742C21.101-0.415,28.604-3.5,37.443-3.5z M37.557,2.272c-7.276,0-13.428,2.553-18.457,7.657    c-5.22,5.334-7.829,11.525-7.829,18.572c0,7.086,2.59,13.22,7.77,18.398c5.181,5.182,11.352,7.771,18.514,7.771    c7.123,0,13.334-2.607,18.629-7.828c5.029-4.838,7.543-10.952,7.543-18.343c0-7.276-2.553-13.465-7.656-18.571    C50.967,4.824,44.795,2.272,37.557,2.272z M46.129,20.557v13.085h-3.656v15.542h-9.944V33.643h-3.656V20.557    c0-0.572,0.2-1.057,0.599-1.457c0.401-0.399,0.887-0.6,1.457-0.6h13.144c0.533,0,1.01,0.2,1.428,0.6    C45.918,19.5,46.129,19.986,46.129,20.557z M33.042,12.329c0-3.008,1.485-4.514,4.458-4.514s4.457,1.504,4.457,4.514    c0,2.971-1.486,4.457-4.457,4.457S33.042,15.3,33.042,12.329z"/>
\t</g>
</g>
</svg><svg style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.0" id="Layer_1" x="0px" y="0px" width="22px" height="22px" viewBox="5.5 -3.5 64 64" enable-background="new 5.5 -3.5 64 64" xml:space="preserve">
<g>
\t<circle fill="#FFFFFF" cx="37.47" cy="28.736" r="29.471"/>
\t<g>
\t\t<path d="M37.442-3.5c8.99,0,16.571,3.085,22.743,9.256C66.393,11.928,69.5,19.509,69.5,28.5c0,8.992-3.048,16.476-9.145,22.458    C53.88,57.32,46.241,60.5,37.442,60.5c-8.686,0-16.19-3.162-22.513-9.485C8.644,44.728,5.5,37.225,5.5,28.5    c0-8.762,3.144-16.343,9.429-22.743C21.1-0.414,28.604-3.5,37.442-3.5z M12.7,19.872c-0.952,2.628-1.429,5.505-1.429,8.629    c0,7.086,2.59,13.22,7.77,18.4c5.219,5.144,11.391,7.715,18.514,7.715c7.201,0,13.409-2.608,18.63-7.829    c1.867-1.79,3.332-3.657,4.398-5.602l-12.056-5.371c-0.421,2.02-1.439,3.667-3.057,4.942c-1.622,1.276-3.535,2.011-5.744,2.2    v4.915h-3.714v-4.915c-3.543-0.036-6.782-1.312-9.714-3.827l4.4-4.457c2.094,1.942,4.476,2.913,7.143,2.913    c1.104,0,2.048-0.246,2.83-0.743c0.78-0.494,1.172-1.312,1.172-2.457c0-0.801-0.287-1.448-0.858-1.943l-3.085-1.315l-3.771-1.715    l-5.086-2.229L12.7,19.872z M37.557,2.214c-7.276,0-13.428,2.571-18.457,7.714c-1.258,1.258-2.439,2.686-3.543,4.287L27.786,19.7    c0.533-1.676,1.542-3.019,3.029-4.028c1.484-1.009,3.218-1.571,5.2-1.686V9.071h3.715v4.915c2.934,0.153,5.6,1.143,8,2.971    l-4.172,4.286c-1.793-1.257-3.619-1.885-5.486-1.885c-0.991,0-1.876,0.191-2.656,0.571c-0.781,0.381-1.172,1.029-1.172,1.943    c0,0.267,0.095,0.533,0.285,0.8l4.057,1.83l2.8,1.257l5.144,2.285l16.397,7.314c0.535-2.248,0.801-4.533,0.801-6.857    c0-7.353-2.552-13.543-7.656-18.573C51.005,4.785,44.831,2.214,37.557,2.214z"/>
\t</g>
</g>
</svg></p>
        <p>DrissionPage<sup>®</sup>为作者已注册的商标　　<a href="https://beian.miit.gov.cn/" target="_blank">粤ICP备2024179482号-1</a>.</p>`,
            },
            prism: {
                theme: prismThemes.github,
                darkTheme: prismThemes.dracula,
            },
            docs: {
                sidebar: {
                    hideable: true,
                },
            },
            algolia: {
                // The application ID provided by Algolia
                appId: '4KZXMJ5S9C',

                // Public API key: it is safe to commit it
                apiKey: '6089da88d67464dcc08d076112429322',

                indexName: 'drissionpage',

                // Optional: see doc section below
                contextualSearch: false,

                // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
//      externalUrlRegex: 'external\\.com|domain\\.com',

                // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
//      replaceSearchResultPathname: {
//        from: '/docs/', // or as RegExp: /\/docs\//
//        to: '/',
//      },

                // Optional: Algolia search parameters
                searchParameters: {},

                // Optional: path for search page that enabled by default (`false` to disable it)
                searchPagePath: 'search',

                //... other Algolia params
            },
            announcementBar: {
                id: 'current_version',
                content: '支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage <b>4.1.0.10</b>',
                backgroundColor: '#3A5FCD',
                textColor: '#FFFFFF',
                isCloseable: true,
            },
        }),
//  plugins: [require.resolve('docusaurus-lunr-search')],

//  plugins: [
////  '@easyops-cn/docusaurus-search-local',
//    [
//      '@easyops-cn/docusaurus-search-local',
//      {
//        hashed: true,
//      },
//    ],
//  ],
};

export default config;
