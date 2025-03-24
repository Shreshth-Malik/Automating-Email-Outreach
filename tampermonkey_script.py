// ==UserScript==
// @name         Auto-Copy Recruiter Info
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Copies name and email from the "meta" section
// @match        Enter website to scrape from (for example http://www.recmails.com/personID=*)
// @grant        GM_setClipboard
// ==/UserScript==

(function() {
    'use strict';

    // Delay to allow dynamic content to load (adjust as needed).
    setTimeout(() => {
        // 1) Grab the name from <h1 class="title"> inside <div class="meta">
        let nameEl = document.querySelector("div.meta h1.title");
        // 2) Grab the email from <a href="mailto:..."> inside <div class="meta">
        let emailEl = document.querySelector("div.meta a[href^='mailto:']");

        if (!nameEl || !emailEl) {
            console.log("Could not find name or email in expected elements.");
            return;
        }

        // Extract text
        let name = nameEl.innerText.trim();
        let firstName = name.split(" ")[0];
        let email = emailEl.innerText.trim();

        // Format "email,name"
        let textToCopy = `${email}, ${firstName}`;

        // Copy to clipboard
        //alert("Click OK to copy the recruiter’s email.");
        navigator.clipboard.writeText(textToCopy)
            .then(() => {
                console.log("Copied to clipboard:", textToCopy);
                // Uncomment if you want an alert popup:
                showToast("Copied: " + textToCopy);
            })
            .catch(err => {
                console.error("Failed to copy:", err);
            });
    }, 200);

    function showToast(message) {
        let toast = document.createElement("div");
        toast.innerText = message;
        toast.style.position = "fixed";
        toast.style.bottom = "20px";
        toast.style.right = "20px";
        toast.style.background = "rgba(0, 0, 0, 0.8)";
        toast.style.color = "#fff";
        toast.style.padding = "10px 20px";
        toast.style.borderRadius = "5px";
        toast.style.fontSize = "14px";
        toast.style.zIndex = "1000";
        toast.style.transition = "opacity 0.5s ease-in-out";

        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.opacity = "0";
            setTimeout(() => toast.remove(), 500);
        }, 2000); // Toast disappears after 2 seconds
    }

})();
