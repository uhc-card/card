.. raw:: html

   <script>
     // Redirect only if on root path like /en/latest/ or /en/stable/
     if (location.pathname.endsWith("/en/latest/") ||
         location.pathname.endsWith("/en/stable/") ||
         location.pathname.match(/\/en\/[^/]+\/$/)) {
       window.location.href = "index.html";
     }
   </script>

   <noscript>
     <meta http-equiv="refresh" content="0; url=index.html">
   </noscript>
