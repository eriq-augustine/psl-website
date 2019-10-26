---
layout: wiki
---

To read in the truth values of ground atoms from text files, a `DataStore` object is required. 

```
DataStore data = new RDBMSDataStore(new H2DatabaseDriver(Type.Disk, "database/path", true), configBundle);
```

In the code snippet above, the `RDBMSDataStore` constructor takes two arguments:
 - H2DatabaseDriver specifying the database to connect to.
 - ConfigBundle specifying additional configuration.

The H2DatabaseDriver constructor accepts three arguments:
 - Type.Disk for a database stored on disk, or Type.Memory for a database held in RAM.
 - The path to store the database (if Type.Disk) is used, or a unique identifier for the database (if Type.Memory).
 - The final boolean indicates whether to clear the contents from any existing database found at the same path (true for clear and false to leave the database intact).

After a `DataStore` is created, we can read in the truth values of ground atoms from text files as follows:

```
Inserter insert = data.getInserter(<predicateName>, <partition>);
InserterUtils.loadDelimitedData(<filePath>);
```

 - `<partition>` is the partition to write the data into.
 - `<predicateName>` is the name of the predicate whose ground atoms are to be read.
 - `<fileName>` is the name of the file containing the ground atoms.

All data read in with `InserterUtils.loadDelimitedData` is assumed to have a truth value of 1.
If you need to also read in specific truth values, use `InserterUtils.loadDelimitedData`.