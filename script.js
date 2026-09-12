const TALLY_FORM_URL = "https://tally.so/r/jagbXJ";

const header = document.querySelector(".site-header");
const waitlistLinks = document.querySelectorAll("[data-waitlist-link]");
const configWarnings = document.querySelectorAll("[data-config-warning]");
const supportEmailLinks = document.querySelectorAll("[data-support-email]");

function updateHeader() {
  if (!header) return;
  header.classList.toggle("is-scrolled", window.scrollY > 24);
}

function configureWaitlistLinks() {
  const isConfigured = !TALLY_FORM_URL.includes("REPLACE_ME");

  configWarnings.forEach((warning) => {
    warning.hidden = isConfigured;
  });

  waitlistLinks.forEach((link) => {
    link.setAttribute("href", TALLY_FORM_URL);

    if (isConfigured) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener");
      return;
    }

    link.addEventListener("click", (event) => {
      event.preventDefault();
      alert("Add your Tally form URL in english-landing/script.js before sharing this page.");
    });
  });
}

function configureSupportEmailLinks() {
  supportEmailLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
      const recipient = ["support", "radimoo.com"].join("@");
      const subject = encodeURIComponent(link.dataset.subject || "radimoo support request");
      const body = encodeURIComponent("Tell us what happened:\n\n");
      window.location.href = `mailto:${recipient}?subject=${subject}&body=${body}`;
    });
  });
}

window.addEventListener("scroll", updateHeader, { passive: true });
updateHeader();
configureWaitlistLinks();
configureSupportEmailLinks();
