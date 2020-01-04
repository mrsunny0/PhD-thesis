# Footnotes
Figures should be followed by footnotemark (before the period). Footnotetext should follow figure enviornment to add data availability

**Example**:
```latex
	some sentence that needs a footnote\footnote{}.

	some sentence in an environment that needs a footnote\protect\footnotemark
	...
	\footnotetext{}
```

# Figure and Table structure
Figure subpanels should be labelled as (\textbf{a,b,c}).

**Example**
```latex
\begin{figure}[H]
	\centering
	\includegraphics[width=\linewidth]{global-waste-map.png}
	\caption[main caption]
	{
		\textbf{main caption}\protect\footnotemark.
		... more caption
  }
	\label{figure:chapter1:global-waste-map}
\end{figure}
\footnotetext{
  data available at: \url{https://datacatalog.worldbank.org/dataset/what-waste-global-database}
}
```

```latex
\begin{table}[H]
	\centering
	\small
	\input{external-table-doc.tex}
	\caption[main caption]
	{
		\textbf{main caption}
		... more caption
  }
	\label{figure:chapter1:global-waste-map}
\end{table}
```

# Labeling and cross-referencing
Package `href` has some bugs when working with the `xr` package. Using `xr-hyper` before implementing the `href` package also introduces some bugs that were hard to identify. Instead, use the `zref` package.

**Example**
```
\label{type:chapter:detail}
```

# Bib and Biblatex(+biber)
https://tex.stackexchange.com/questions/41821/creating-bib-file-containing-only-the-cited-references-of-a-bigger-bib-file

# Annotations
```
%---------------------------------------------------------------------------%
%                                   BREAK                                   %
%---------------------------------------------------------------------------%
```

```
%***************************************************************************%
%                                 CHAPTER X                                 %
%***************************************************************************%
```

```
%===========================================================================%
% SECTION
%===========================================================================%
```

```
%-----------------------------------------------------------------%
% SUBSECTION
%-----------------------------------------------------------------%
```

```
%.......................................................%
% SUBSUBSECTION
%.......................................................%
```

```
%===============%
% FIGURES
%===============%
```

```
%~~~~~~~~~~~~~~~%
% TABLES
%~~~~~~~~~~~~~~~%
```

```
%:::::::::::::::%
% EQUATIONS
%:::::::::::::::%
```

```
%...............%
% INPUT
%...............%
```

```
%---------------%
% SPECIFIC NOTE
%---------------%
```

```
%===============================BIBLIOGRAPHY================================%
```

```
% all comments should be lower cased, unless denoting a particular section (e.g. Chapter inputs)
```

```
% comment
```

```
%% comment heading
```

```
%/ block comment
%| ...
%| ...
%| ...
%\ block comment
```
