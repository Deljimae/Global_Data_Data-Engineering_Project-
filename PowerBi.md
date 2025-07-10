# 📊 Power BI: Connecting to Amazon Athena via ODBC

This guide details how to connect **Power BI** to an **Amazon Athena** database using an **ODBC driver**, ideal for analysts and BI developers.

---

## 📚 Table of Contents

1. [🧾 Prerequisites](#1-prerequisites)  
2. [🖥 Power BI Desktop Setup](#2-power-bi-desktop-setup)  
   - [2.1. Download and Install the ODBC Driver](#21-download-and-install-the-odbc-driver)  
   - [2.2. Configure the ODBC Connector](#22-configure-the-odbc-connector)  
   - [2.3. Connect in Power BI](#23-connect-in-power-bi)
3. [🚪 Power BI Gateway Setup (for scheduled refresh)](#3-power-bi-gateway-setup)
4. [⚠️ Important Considerations](#4-important-considerations)

---

## 1. 🧾 Prerequisites

Before you connect Power BI to Athena, ensure you have the following:

- ✅ **AWS Access Key** and **Secret Key**
- 🌍 **Region** (e.g., `us-east-1`)
- 🪣 **S3 Output Bucket Location** (e.g., `s3://your-output-bucket/`)
- 🗃 **Athena Database Name** (e.g., `kestradb`)
- ⚙️ **Athena Workgroup Name** (e.g., `primary`)
- 🔍 *(Optional)*: Table or view names to query

> 💡 Note: Power BI does **not** support writing custom SQL against Athena directly. Create views or tables in Athena first.

---

## 2. 🖥 Power BI Desktop Setup

### 2.1. Download and Install the ODBC Driver

1. Search for **“AWS Athena ODBC Driver”** or visit the [official AWS ODBC documentation](https://docs.aws.amazon.com/athena/latest/ug/athena-odbc.html).
2. Choose the appropriate installer for your OS (typically **Windows 64-bit**).
3. Run the installer with default settings.

---

### 2.2. Configure the ODBC Connector

1. Open **ODBC Data Source Administrator (64-bit)**
2. Go to the **System DSN** tab → click **Add...**
3. Select **Simba Athena ODBC Driver** → click **Finish**
4. Fill in the DSN setup:
   - **Data Source Name**: `CloudTRData` (or any name)
   - **Region**: `us-east-1`
   - **Catalog**: `AwsDataCatalog` (default)
   - **Schema**: `kestradb` (your Athena database)
   - **Workgroup**: `primary`
   - **S3 Output Location**: `s3://your-output-bucket/`
5. Click **Authentication Options...**:
   - **Method**: `Access Key`
   - **Access Key**: Paste your access key
   - **Secret Key**: Paste your secret key
6. Click **OK**
7. Click **Test** → You should see: ✅ *Connection Successful*
8. Click **OK** to save

---

### 2.3. Connect in Power BI

1. Open **Power BI Desktop**
2. Click **Get Data** → select **ODBC** → click **Connect**
3. From the DSN dropdown, select your DSN (e.g., `CloudTRData`)
4. When prompted:
   - **Username**: *Access Key*
   - **Password**: *Secret Key*
5. Click **Connect**
6. In the **Navigator**, expand:
   - `AwsDataCatalog`
   - Your schema/database (e.g., `kestradb`)
7. Select a **table** or **view** → click **Load**

---

## 3. 🚪 Power BI Gateway Setup

To schedule data refresh:

1. Install the **same ODBC driver** on your Power BI Gateway machine.
2. Create the **same DSN** as used on your local machine.

In **Power BI Service** → add a new data source under Gateway settings:

- **Connection String**:  
  `DSN=CloudTRData`
- **Authentication Method**:  
  `Basic`
- **Username**: *Access Key*  
- **Password**: *Secret Key*
- Click **Add**

---

## 4. ⚠️ Important Considerations

- 🌀 **Serverless engine**: Athena performance is managed by AWS — expect variable latency.
- 🔐 **Authentication Security**: For production, consider:
  - IAM roles
  - Instance profiles
  - Federated identity (e.g., ADFS)
- 🛠 **Troubleshooting**:
  - Double-check:
    - ✅ Region
    - ✅ Catalog (`AwsDataCatalog`)
    - ✅ Schema (`kestradb`)
    - ✅ Workgroup
    - ✅ S3 bucket path
  - Use Athena console to test queries independently.

---

> 📎 *Maintained by: Ayodeji Lana*  
> 🔗 *Project Repository*: [Global_Data_Data-Engineering_Project](https://github.com/Deljimae/Global_Data_Data-Engineering_Project-)

