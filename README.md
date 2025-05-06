# Import Excel File which was a DSS export, and look at wanted output format for XPSWMM External data

### The DSS data is exported to Excel via DSSVue and then can be read into python using pandas

Station IDs were assigned in the excel file along the header row to use instead of the DSS B-PART. The Station ID matches the node ID witin the XPSWMM model.

![image](https://github.com/user-attachments/assets/69c22e1f-b17a-439e-9afc-a0a4db765214)

#### Format the data
The data is then formatted and output to XPSWMM's required textfile format of [Value, ID] and written to disk.

![image](https://github.com/user-attachments/assets/0b62f062-a507-4888-a4c1-69702f5c7401)


