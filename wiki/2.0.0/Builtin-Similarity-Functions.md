---
layout: wiki
---

PSL comes with several builtin similarity functions. If you have a need not captured by these functions, then you can also create [customized similarity functions](External-Functions.md).

These similarity functions are shipped with the [PSL Utils](https://github.com/linqs/psl-utils) package.

## Text Similarity

**Name**: Cosine Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.CosineSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://en.wikipedia.org/wiki/Cosine_similarity  

**Name**: Dice Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.DiceSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient

**Name**: Jaccard Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.JaccardSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://en.wikipedia.org/wiki/Jaccard_index  

**Name**: Jaro Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.JaroSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://www.census.gov/srd/papers/pdf/rr91-9.pdf  

**Name**: Jaro-Winkler Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.JaroWinklerSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance  

**Name**: Level 2 Jaro-Winkler Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.Level2JaroWinklerSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: A level 2 variation of Jaro-Winkler Similarity. Level 2 means that tokens are broken up before comparison (see http://secondstring.sourceforge.net/javadoc/com/wcohen/ss/Level2.html).  

**Name**: Level 2 Levenshtein Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.Level2LevenshteinSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: A level 2 variation of Levenshtein Similarity. Level 2 means that tokens are broken up before comparison (see http://secondstring.sourceforge.net/javadoc/com/wcohen/ss/Level2.html).  

**Name**: Level 2 Monge Elkan Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.Level2MongeElkanSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://www.aaai.org/Papers/KDD/1996/KDD96-044.pdf  

**Name**: Levenshtein Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.LevenshteinSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: https://en.wikipedia.org/wiki/Levenshtein_distance  

**Name**: Same Initials  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.SameInitials  
**Arguments**: String, String  
**Return Type**: Discrete  
**Description**: First splits the input strings on any whitespace and ensures both have the same number of tokens (returns 0 if they do not). Then, the first character of all the tokens are checked for equality (ignoring case and order of appearance). Note that all all character that are not alphabetic ASCII characters are considered equal (eg. all numbers and unicode are considered the same character).  

**Name**: Same Number of Tokens  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.SameNumTokens  
**Arguments**: String, String  
**Return Type**: Discrete  
**Description**: Checks same number of tokens (delimited by any whitespace).  

**Name**: Sub String Similarity  
**Qualified Path**: org.linqs.psl.utils.textsimilarity.SubStringSimilarity  
**Arguments**: String, String  
**Return Type**: Continuous  
**Description**: If one input string is a substring of another, then the length of the substring divided by the length of the text is returned. 0 is returned if neither string is a substring of the other.  