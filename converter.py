<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Comparison Table</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            margin: 0;
            padding: 20px;
            background-color: #0E1119; /* TeamStation AI Dark Background */
            color: #FFFFFF; /* White font color for body text */
            line-height: 1.6;
        }
        .table-container {
            overflow-x: auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5); /* Enhanced shadow for depth on dark bg */
            border-radius: 8px;
            border: 1px solid #2A2F3A; /* Slightly lighter border for definition */
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 800px;
        }
        caption {
            font-size: 1.5em;
            margin-bottom: 1em;
            font-weight: bold;
            color: #88C0D0; /* A light, desaturated blue for caption - good contrast */
            text-align: left;
        }
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #2A2F3A; /* Border color matching container border */
            vertical-align: top;
            color: #E0E0E0; /* Slightly off-white for main table text for softer look */
        }
        th {
            background-color: #1A202C; /* Darker shade for headers */
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.05em;
            position: sticky;
            top: 0;
            z-index: 10;
            color: #FFFFFF; /* Ensure header text is bright white */
        }
        tr:hover td:not(.category-header) {
            background-color: #2A2F3A; /* Hover color */
        }
        .category-header {
            background-color: #0A0D14; /* Even darker for category headers, close to bg */
            color: #A7D2CB; /* Light Teal/Cyan for category header text */
            font-weight: bold;
            font-size: 1.1em;
            text-align: center;
        }
        .feature-name {
            font-weight: 500;
            min-width: 200px;
            color: #FFFFFF; /* Bright white for feature names for emphasis */
        }
        .icon-text {
            display: inline-block;
            margin-right: 8px;
            font-weight: bold;
            font-size: 1.1em;
            width: 20px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div class="table-container">
        <table>
            <caption>Service Clarity Comparison</caption>
            <thead>
                <tr>
                    <th>Service/Feature</th>
                    <th>TeamStation AI</th>
                    <th>Traditional Legacy Nearshore IT Staffing Vendors</th>
                    <th>Nearshore/Global EOR Service/Online Platforms</th>
                </tr>
            </thead>
            <tbody>
                <!-- Data will be populated here by JavaScript -->
            </tbody>
        </table>
    </div>

<script>
const comparisonData = [
  {
    name: "TALENT ACQUISITION & ONBOARDING",
    features: [
      {
        name: "Candidate Sourcing",
        teamStationAI: "AI-Powered Global Pool, Rapid Matching",
        traditionalVendor: "Manual Sourcing, Local Networks",
        eorPlatform: "Platform-Based Job Postings, Varies"
      },
      {
        name: "Skill Assessment & Vetting",
        teamStationAI: "Automated Skills Tests, AI Behavioral Analysis",
        traditionalVendor: "Manual Interviews, Subjective Evaluation",
        eorPlatform: "Basic Online Tests, Self-Reported Skills"
      },
      {
        name: "Background & Compliance Checks",
        teamStationAI: "Comprehensive, Automated, Fast Turnaround",
        traditionalVendor: "Standard Checks, Slower Process",
        eorPlatform: "Varies by Provider, Often Basic"
      },
      {
        name: "Onboarding & Integration",
        teamStationAI: "Streamlined Digital Onboarding, AI-Assisted Team Integration",
        traditionalVendor: "Manual Paperwork, Ad-hoc Integration",
        eorPlatform: "Platform-Guided, Limited Customization"
      },
    ],
  },
  {
    name: "OPERATIONAL EFFICIENCY & MANAGEMENT",
    features: [
      {
        name: "Project Management Tools",
        teamStationAI: "Integrated Suite with AI Task Management",
        traditionalVendor: "Client Provides Tools or Basic Tracking",
        eorPlatform: "Typically None, Relies on Client"
      },
      {
        name: "Communication & Collaboration Platform",
        teamStationAI: "Unified Platform, Real-time Translation, AI Summaries",
        traditionalVendor: "Email, Phone, Ad-hoc Tools",
        eorPlatform: "Basic Messaging, Limited Features"
      },
      {
        name: "Performance Monitoring & Reporting",
        teamStationAI: "AI-Driven Insights, Predictive Analytics, Real-time Dashboards",
        traditionalVendor: "Manual Reporting, Weekly/Monthly Updates",
        eorPlatform: "Simple Time Tracking, Basic Reports"
      },
      {
        name: "Knowledge Management & Transfer",
        teamStationAI: "AI-Powered Knowledge Base, Automated Documentation",
        traditionalVendor: "Relies on Individuals, Manual Documentation",
        eorPlatform: "None or Basic File Sharing"
      }
    ],
  },
  {
    name: "COST, CONTRACTING & SCALABILITY",
    features: [
      {
        name: "Pricing Model & Transparency",
        teamStationAI: "Transparent, All-Inclusive, Value-Based",
        traditionalVendor: "Hourly Rates + Markups, Often Opaque",
        eorPlatform: "Subscription + % of Salary, Potential Hidden Fees"
      },
      {
        name: "Contract Flexibility & Scalability",
        teamStationAI: "Highly Flexible, On-demand Scaling (Up/Down)",
        traditionalVendor: "Fixed-Term Contracts, Rigid Scaling",
        eorPlatform: "Varies, Termination Fees Common, Scaling Can Be Slow"
      },
      {
        name: "Time to Productivity",
        teamStationAI: "Rapid (Days to 1-2 Weeks)",
        traditionalVendor: "Moderate (Weeks to Months)",
        eorPlatform: "Varies, Can be Quick for Simple Roles"
      },
      {
        name: "Risk & Compliance Management",
        teamStationAI: "Proactive AI-Monitored Compliance, Shared Responsibility",
        traditionalVendor: "Client Bears Most Risk, Reactive",
        eorPlatform: "EOR Handles Payroll/Tax Compliance, Other Risks May Remain"
      }
    ],
  },
];

function getCellClassAndIcon(text) {
    const lowerText = text.toLowerCase();
    // Icons will inherit the white/off-white text color from the td/th by default.
    // We only need to change the symbol itself and potentially override color for emphasis.
    let iconSymbol = '●'; // Default info icon symbol
    let iconStyle = 'color: #A7D2CB;'; // Default icon color (light teal/cyan)

    if (
        lowerText.includes("ai-powered") ||
        lowerText.includes("comprehensive") ||
        lowerText.includes("automated") ||
        lowerText.includes("streamlined") ||
        lowerText.includes("unified") ||
        lowerText.includes("transparent") ||
        lowerText.includes("flexible") ||
        lowerText.includes("rapid") ||
        lowerText.includes("all-inclusive") ||
        lowerText.includes("proactive") ||
        lowerText.includes("integrated suite")
    ) {
        iconSymbol = '✔'; 
        iconStyle = 'color: #50C878;'; // Emerald Green for positive
    } else if (
        lowerText.includes("not included") ||
        lowerText.includes("none") ||
        lowerText.includes("limited features") ||
        lowerText.includes("relies on client") ||
        lowerText.includes("opaque") ||
        lowerText.includes("rigid") ||
        lowerText.includes("reactive") ||
        lowerText.includes("typically none")
    ) {
        iconSymbol = '✘';
        iconStyle = 'color: #FF6B6B;'; // Light Red for negative
    } else if (
        lowerText.includes("varies") ||
        lowerText.includes("manual") ||
        lowerText.includes("basic") ||
        lowerText.includes("standard") ||
        lowerText.includes("often") ||
        lowerText.includes("subjective") ||
        lowerText.includes("ad-hoc") ||
        lowerText.includes("moderate") ||
        lowerText.includes("potential") ||
        lowerText.includes("common") ||
        lowerText.includes("may remain") ||
        lowerText.includes("slower process") ||
        lowerText.includes("limited customization")
    ) {
        iconSymbol = '~'; 
        iconStyle = 'color: #B0BEC5;'; // Lighter Gray for neutral
    }
    
    return { iconHtml: `<span class="icon-text" style="${iconStyle}">${iconSymbol}</span>` };
}

const tableBody = document.querySelector('table tbody');
comparisonData.forEach(category => {
    const categoryRow = tableBody.insertRow();
    const categoryCell = categoryRow.insertCell();
    categoryCell.colSpan = 4; 
    categoryCell.className = 'category-header';
    categoryCell.textContent = category.name;

    category.features.forEach(feature => {
        const featureRow = tableBody.insertRow();
        const nameCell = featureRow.insertCell();
        nameCell.className = 'feature-name';
        nameCell.textContent = feature.name;

        const tsCell = featureRow.insertCell();
        const tsInfo = getCellClassAndIcon(feature.teamStationAI);
        tsCell.innerHTML = tsInfo.iconHtml + ' ' + feature.teamStationAI;

        const tvCell = featureRow.insertCell();
        const tvInfo = getCellClassAndIcon(feature.traditionalVendor);
        tvCell.innerHTML = tvInfo.iconHtml + ' ' + feature.traditionalVendor;

        const eorCell = featureRow.insertCell();
        const eorInfo = getCellClassAndIcon(feature.eorPlatform);
        eorCell.innerHTML = eorInfo.iconHtml + ' ' + feature.eorPlatform;
    });
});
</script>

</body>
</html>
