(function(){"use strict";try{if(typeof document<"u"){var o=document.createElement("style");o.appendChild(document.createTextNode(".mycomponent{max-width:1280px;margin:0 auto;padding:2rem;text-align:center}.mycomponent .card{padding:2em}.mycomponent{font-family:Inter,system-ui,Avenir,Helvetica,Arial,sans-serif;line-height:1.5;font-weight:400;color-scheme:light dark;color:#ffffffde;background-color:#242424;font-synthesis:none;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;-webkit-text-size-adjust:100%}.mycomponent a{font-weight:500;color:#646cff;text-decoration:inherit}.mycomponent a:hover{color:#535bf2}.mycomponent h1{font-size:3.2em;line-height:1.1}.mycomponent button{border-radius:8px;border:1px solid transparent;padding:.6em 1.2em;font-size:1em;font-weight:500;font-family:inherit;background-color:#1a1a1a;cursor:pointer;transition:border-color .25s}.mycomponent button:hover{border-color:#646cff}.mycomponent>button:focus,.mycomponent>button:focus-visible{outline:4px auto -webkit-focus-ring-color}@media (prefers-color-scheme: light){.mycomponent{color:#213547;background-color:#fff}.mycomponent a:hover{color:#747bff}.mycomponent button{background-color:#f9f9f9}}")),document.head.appendChild(o)}}catch(e){console.error("vite-plugin-css-injected-by-js",e)}})();
var wmc=function(n,e,i){"use strict";const w="";function m({passSetters:t,setOutput:d,renderInit:c}){const[s,r]=e.useState(c),[o,l]=e.useState(0);return e.useEffect(()=>{t({onInput:l,onRender:r})},[l,r,t]),s?e.createElement(e.Fragment,null,e.createElement("h1",null,"Windmill Custom Component"),e.createElement("div",{className:"card"},e.createElement("button",{className:"mr-4",onClick:()=>l(a=>a+1)},"input count is ",o),e.createElement("button",{onClick:()=>d(o)},"Setting output to ",o))):e.createElement(e.Fragment,null)}const E="";function u(t){i.createRoot(document.getElementById(t.id)).render(e.createElement(e.StrictMode,null,e.createElement(m,{passSetters:t.passSetters,setOutput:t.setOutput,renderInit:t.render})))}return window.windmill===void 0&&(window.windmill={}),window.windmill.mycomponent=u,n.customComponent=u,Object.defineProperty(n,Symbol.toStringTag,{value:"Module"}),n}({},React,ReactDOM);