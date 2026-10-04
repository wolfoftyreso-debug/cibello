export const COMPANY = {
  legalName: "LandveX AB",
  brand: "Cibello",
  orgNr: "559141-7042",
  vatId: "SE559141704201",
  street: "Antennvägen 2",
  postalCode: "135 48",
  city: "Tyresö",
  country: "SE",
  countryName: "Sverige",
  phoneE164: "+46101985881",
  phoneDisplay: "+46 10 198 58 81",
  email: "contact@cibello.app",
  supportEmail: "support@cibello.app",
  privacyEmail: "privacy@cibello.app",
  parentEmail: "contact@landvex.com",
  parentUrl: "https://landvex.com",
  url: "https://cibello.app/",
} as const;

export const COMPANY_ADDRESS = `${COMPANY.street}, ${COMPANY.postalCode} ${COMPANY.city}`;

export const COMPANY_LINE = `${COMPANY.brand} · ${COMPANY.legalName} · Org.nr ${COMPANY.orgNr} · ${COMPANY_ADDRESS} · Momsnr ${COMPANY.vatId} · Byggd i Sverige.`;

export function organizationJsonLd() {
  return {
    "@type": "Organization",
    "@id": "https://cibello.app/#organization",
    name: COMPANY.legalName,
    legalName: COMPANY.legalName,
    alternateName: COMPANY.brand,
    url: COMPANY.url,
    email: COMPANY.email,
    telephone: COMPANY.phoneE164,
    vatID: COMPANY.vatId,
    identifier: {
      "@type": "PropertyValue",
      propertyID: "Swedish company registration number",
      value: COMPANY.orgNr,
    },
    address: {
      "@type": "PostalAddress",
      streetAddress: COMPANY.street,
      postalCode: COMPANY.postalCode,
      addressLocality: COMPANY.city,
      addressCountry: COMPANY.country,
    },
    contactPoint: {
      "@type": "ContactPoint",
      contactType: "customer support",
      telephone: COMPANY.phoneE164,
      email: COMPANY.email,
      areaServed: "SE",
      availableLanguage: ["sv", "en", "de", "fr", "es", "it", "nl", "pl", "da", "nb", "fi", "pt"],
    },
    sameAs: [
      "https://www.facebook.com/profile.php?id=61593336222919",
      "https://www.instagram.com/cibelloapp/",
      "https://www.tiktok.com/@cibello_recipes",
      "https://www.pinterest.com/cibelloapp/",
      "https://www.youtube.com/@cibelloappofficial",
      "https://apps.apple.com/app/id6807100747",
      "https://play.google.com/store/apps/details?id=com.cibello.app",
    ],
    brand: { "@type": "Brand", name: COMPANY.brand },
  };
}
