---
layout: page
title: "A Random Process"
date: 2021-06-14
tags: Probability, Numpy
key: "RP-1406"
comment: true
---
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>3.RandomProcess</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0px solid transparent;
  border-right: 0px solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
	border:1px solid transparent;
  background-color: transparent;
  position: absolute;
	z-index:1;
	right:3%;
	top: 0;
	bottom: 0;
	margin: auto;
	padding: 7px 0;
	display: none;
	vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
	content: "X";
	display: block;
	width: 15px;
	height: 15px;
	text-align: center;
	color:#000;
	font-weight: normal;
	font-size: 12px;
	cursor: pointer;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
  background: inherit;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

@charset "UTF-8";
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-bottom:10px;
  margin-top:0; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  font-size:36px;
  line-height:40px; }

h2.bp3-heading, .bp3-running-text h2{
  font-size:28px;
  line-height:32px; }

h3.bp3-heading, .bp3-running-text h3{
  font-size:22px;
  line-height:25px; }

h4.bp3-heading, .bp3-running-text h4{
  font-size:18px;
  line-height:21px; }

h5.bp3-heading, .bp3-running-text h5{
  font-size:16px;
  line-height:19px; }

h6.bp3-heading, .bp3-running-text h6{
  font-size:14px;
  line-height:16px; }
.bp3-ui-text{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none; }

.bp3-monospace-text{
  font-family:monospace;
  text-transform:none; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  font-size:14px;
  line-height:1.5; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15);
    margin:20px 0; }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  color:#106ba3;
  text-decoration:none; }
  a:hover{
    color:#106ba3;
    cursor:pointer;
    text-decoration:underline; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  font-size:smaller;
  padding:2px 5px; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  color:#182026;
  display:block;
  font-size:13px;
  line-height:1.4;
  margin:10px 0;
  padding:13px 15px 12px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit;
    font-size:inherit;
    padding:0; }

.bp3-running-text kbd, .bp3-key{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-family:inherit;
  font-size:12px;
  height:24px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  line-height:24px;
  min-width:24px;
  padding:3px 6px;
  vertical-align:middle; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  margin:0 0 10px;
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    font-size:40px;
    margin-right:20px;
    margin-top:0; }

.bp3-alert-contents{
  word-break:break-word; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  cursor:default;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  height:30px;
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-breadcrumbs > li{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }
    .bp3-breadcrumbs > li::after{
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 00-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      content:"";
      display:block;
      height:16px;
      margin:0 5px;
      width:16px; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    font-size:inherit;
    font-weight:inherit;
    vertical-align:baseline; }

.bp3-breadcrumbs-collapsed{
  background:#ced9e0;
  border:none;
  border-radius:3px;
  cursor:pointer;
  margin-right:2px;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    content:"";
    display:block;
    height:16px;
    width:16px; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    color:#182026;
    text-decoration:none; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  min-height:30px;
  min-width:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      background-color:#106ba3;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      background-color:#0e5a8a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      background-color:#0d8050;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      background-color:#0a6640;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      background-color:#bf7326;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      background-color:#a66321;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      background-color:#c23030;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      background-color:#a82a2a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-height:40px;
    min-width:40px;
    font-size:16px;
    padding:5px 15px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      margin:0;
      position:absolute; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button.bp3-minimal:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button.bp3-outlined{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    border:1px solid rgba(24, 32, 38, 0.2);
    -webkit-box-sizing:border-box;
            box-sizing:border-box; }
    .bp3-button.bp3-outlined:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-outlined:active, .bp3-button.bp3-outlined.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-outlined{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-outlined:hover, .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-outlined:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover, .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover, .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover, .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover, .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled:hover{
      border-color:rgba(92, 112, 128, 0.1); }
    .bp3-dark .bp3-button.bp3-outlined{
      border-color:rgba(255, 255, 255, 0.4); }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        border-color:rgba(255, 255, 255, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      border-color:rgba(16, 107, 163, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        border-color:rgba(16, 107, 163, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        border-color:rgba(72, 175, 240, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          border-color:rgba(72, 175, 240, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      border-color:rgba(13, 128, 80, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        border-color:rgba(13, 128, 80, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        border-color:rgba(61, 204, 145, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          border-color:rgba(61, 204, 145, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      border-color:rgba(191, 115, 38, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        border-color:rgba(191, 115, 38, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        border-color:rgba(255, 179, 102, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          border-color:rgba(255, 179, 102, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      border-color:rgba(194, 48, 48, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        border-color:rgba(194, 48, 48, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        border-color:rgba(255, 115, 115, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          border-color:rgba(255, 115, 115, 0.2); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    border-bottom-right-radius:0;
    border-top-right-radius:0;
    margin-right:-1px; }
  .bp3-button-group.bp3-minimal .bp3-button{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      height:100%;
      width:unset; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  font-size:14px;
  line-height:1.5;
  background-color:rgba(138, 155, 168, 0.15);
  border-radius:3px;
  padding:10px 12px 9px;
  position:relative;
  width:100%; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout .bp3-heading{
    line-height:20px;
    margin-bottom:5px;
    margin-top:0; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  opacity:0.9;
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  width:100%; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }

.bp3-dialog{
  background:#ebf1f5;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text;
  width:500px; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    background:#293742;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-dialog-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding-left:20px;
  padding-right:5px;
  z-index:30; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    background:#30404d;
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  margin:20px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-multistep-dialog-panels{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }

.bp3-multistep-dialog-left-panel{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column; }
  .bp3-dark .bp3-multistep-dialog-left-panel{
    background:#202b33; }

.bp3-multistep-dialog-right-panel{
  background-color:#f5f8fa;
  border-left:1px solid rgba(16, 22, 26, 0.15);
  border-radius:0 0 6px 0;
  -webkit-box-flex:3;
      -ms-flex:3;
          flex:3;
  min-width:0; }
  .bp3-dark .bp3-multistep-dialog-right-panel{
    background-color:#293742;
    border-left:1px solid rgba(16, 22, 26, 0.4); }

.bp3-multistep-dialog-footer{
  background-color:#ffffff;
  border-radius:0 0 6px 0;
  border-top:1px solid rgba(16, 22, 26, 0.15);
  padding:10px; }
  .bp3-dark .bp3-multistep-dialog-footer{
    background:#30404d;
    border-top:1px solid rgba(16, 22, 26, 0.4); }

.bp3-dialog-step-container{
  background-color:#f5f8fa;
  border-bottom:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-dialog-step-container{
    background:#293742;
    border-bottom:1px solid rgba(16, 22, 26, 0.4); }
  .bp3-dialog-step-container.bp3-dialog-step-viewed{
    background-color:#ffffff; }
    .bp3-dark .bp3-dialog-step-container.bp3-dialog-step-viewed{
      background:#30404d; }

.bp3-dialog-step{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#f5f8fa;
  border-radius:6px;
  cursor:not-allowed;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:4px;
  padding:6px 14px; }
  .bp3-dark .bp3-dialog-step{
    background:#293742; }
  .bp3-dialog-step-viewed .bp3-dialog-step{
    background-color:#ffffff;
    cursor:pointer; }
    .bp3-dark .bp3-dialog-step-viewed .bp3-dialog-step{
      background:#30404d; }
  .bp3-dialog-step:hover{
    background-color:#f5f8fa; }
    .bp3-dark .bp3-dialog-step:hover{
      background:#293742; }

.bp3-dialog-step-icon{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:rgba(92, 112, 128, 0.6);
  border-radius:50%;
  color:#ffffff;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:25px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:25px; }
  .bp3-dark .bp3-dialog-step-icon{
    background-color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#2b95d6; }
  .bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#8a9ba8; }

.bp3-dialog-step-title{
  color:rgba(92, 112, 128, 0.6);
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  padding-left:10px; }
  .bp3-dark .bp3-dialog-step-title{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-title{
    color:#2b95d6; }
  .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
    color:#182026; }
    .bp3-dark .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
      color:#f5f8fa; }
.bp3-drawer{
  background:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    height:50%;
    left:0;
    right:0;
    top:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-bottom{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-left{
    bottom:0;
    left:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-right{
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    background:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-drawer-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding:5px;
  padding-left:20px;
  position:relative; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  overflow:auto; }

.bp3-drawer-footer{
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  padding:10px 20px;
  position:relative; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  cursor:text;
  display:inline-block;
  max-width:100%;
  position:relative;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    bottom:-3px;
    left:-3px;
    position:absolute;
    right:-3px;
    top:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  color:inherit;
  display:inherit;
  font:inherit;
  letter-spacing:inherit;
  max-width:inherit;
  min-width:inherit;
  position:relative;
  resize:none;
  text-transform:inherit;
  vertical-align:top; }

.bp3-editable-text-input{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0;
  white-space:pre-wrap;
  width:100%; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    left:0;
    position:absolute;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    border-radius:inherit;
    z-index:2; }
    .bp3-control-group .bp3-input:focus{
      border-radius:3px;
      z-index:14; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    border-radius:inherit;
    z-index:4; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-left-container,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group .bp3-select:focus-within{
    z-index:5; }
  .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:-1px; }
  .bp3-control-group:not(.bp3-vertical) > .bp3-divider:not(:first-child){
    margin-left:6px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    border-radius:0 3px 3px 0;
    margin-right:0; }
  .bp3-control-group > :only-child{
    border-radius:3px;
    margin-right:0; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group .bp3-numeric-input:not(:first-child) .bp3-input-group{
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-control-group.bp3-fill{
    width:100%; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      border-radius:3px 3px 0 0;
      margin-top:0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  cursor:pointer;
  display:block;
  margin-bottom:10px;
  position:relative;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    left:0;
    opacity:0;
    position:absolute;
    top:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    cursor:pointer;
    display:inline-block;
    font-size:16px;
    height:1em;
    margin-right:10px;
    margin-top:-3px;
    position:relative;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none;
    vertical-align:middle;
    width:1em; }
    .bp3-control .bp3-control-indicator::before{
      content:"";
      display:block;
      height:1em;
      width:1em; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    background:#d8e1e8;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-left:10px;
    margin-top:1px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 00-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0012 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:auto; }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      background:#ffffff;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      height:calc(1em - 4px);
      left:0;
      margin:2px;
      position:absolute;
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      width:calc(1em - 4px); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    font-size:0.7em;
    text-align:center; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    line-height:0;
    margin-left:0.5em;
    margin-right:1.2em;
    visibility:hidden; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    line-height:1em;
    margin-left:1.2em;
    margin-right:0.5em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    line-height:1em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    line-height:0;
    visibility:hidden; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      background:#202b33;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  cursor:pointer;
  display:inline-block;
  height:30px;
  position:relative; }
  .bp3-file-input input{
    margin:0;
    min-width:200px;
    opacity:0; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      background:rgba(206, 217, 224, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(92, 112, 128, 0.6);
        cursor:not-allowed;
        outline:none; }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        background:rgba(57, 75, 89, 0.5);
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          -webkit-box-shadow:none;
                  box-shadow:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:rgba(92, 112, 128, 0.6);
  left:0;
  padding-right:80px;
  position:absolute;
  right:0;
  top:0;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-file-upload-input::after{
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026;
    min-height:24px;
    min-width:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    border-radius:3px;
    content:"Browse";
    line-height:24px;
    margin:3px;
    position:absolute;
    right:0;
    text-align:center;
    top:0;
    width:70px; }
    .bp3-file-upload-input::after:hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-file-upload-input:active::after{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-large .bp3-file-upload-input{
    font-size:16px;
    height:40px;
    line-height:40px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-height:30px;
      min-width:30px;
      line-height:30px;
      margin:5px;
      width:85px; }
  .bp3-dark .bp3-file-upload-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        background-color:#30404d;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        background-color:#202b33;
        background-image:none;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:active::after{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    color:#5c7080;
    font-size:12px;
    margin-top:5px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      line-height:40px;
      margin:0 10px 0 0; }
    .bp3-form-group.bp3-inline label.bp3-label{
      line-height:30px;
      margin:0 10px 0 0; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-input-left-container:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-input-left-container:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-height:24px;
    min-width:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-icon{
    z-index:1; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon{
    color:#5c7080; }
    .bp3-input-group > .bp3-input-left-container > .bp3-icon:empty,
    .bp3-input-group > .bp3-icon:empty{
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-height:30px;
    min-width:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle; }
  .bp3-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-input.bp3-large{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-bottom:15px;
  margin-top:0; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    font-weight:400;
    vertical-align:top;
    width:100%; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  min-height:0;
  padding:0;
  width:30px; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  -moz-appearance:none;
  -webkit-appearance:none;
  border-radius:3px;
  height:30px;
  padding:0 25px 0 10px;
  width:100%; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  background:none;
  -webkit-box-shadow:none;
          box-shadow:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    background:rgba(167, 182, 194, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026;
    text-decoration:none; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    background:rgba(115, 134, 148, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      color:rgba(167, 182, 194, 0.6);
      cursor:not-allowed; }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  font-size:16px;
  height:40px;
  padding-right:35px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    background-color:#202b33;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  background-color:rgba(206, 217, 224, 0.5);
  -webkit-box-shadow:none;
          box-shadow:none;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  color:#5c7080;
  pointer-events:none;
  position:absolute;
  right:7px;
  top:7px; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  letter-spacing:normal;
  position:relative;
  vertical-align:middle; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    right:12px;
    top:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select option:disabled, .bp3-dark
  .bp3-select option:disabled{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    text-align:left;
    vertical-align:top; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td,
  .bp3-running-text table tfoot tr:first-child th,
  table.bp3-html-table tfoot tr:first-child th,
  .bp3-running-text table tfoot tr:first-child td,
  table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td,
  .bp3-dark .bp3-running-text table tfoot tr:first-child th,
  .bp3-running-text .bp3-dark table tfoot tr:first-child th,
  .bp3-dark table.bp3-html-table tfoot tr:first-child th,
  .bp3-dark .bp3-running-text table tfoot tr:first-child td,
  .bp3-running-text .bp3-dark table tfoot tr:first-child td,
  .bp3-dark table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-bottom:6px;
  padding-top:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td,
table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
  table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table{ }
  .bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
    background:rgba(92, 112, 128, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td,
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
      -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
              box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
    background-color:rgba(92, 112, 128, 0.3);
    cursor:pointer; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
    background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  padding-bottom:0;
  top:40px; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-left:0;
  margin-right:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  font-family:"Icons20";
  font-size:inherit;
  font-style:normal;
  font-weight:400;
  line-height:1; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagnosis::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-lab-test::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }
  .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{ }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  background:#ffffff;
  border-radius:3px;
  color:#182026;
  list-style:none;
  margin:0;
  min-width:180px;
  padding:5px;
  text-align:left; }

.bp3-menu-divider{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px; }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  color:inherit;
  line-height:20px;
  padding:5px 7px;
  text-decoration:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    color:#5c7080;
    margin-top:2px; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit !important;
    color:rgba(92, 112, 128, 0.6) !important;
    cursor:not-allowed !important;
    outline:none !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    font-size:16px;
    line-height:22px;
    padding:9px 7px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-right:10px;
      margin-top:1px; }

button.bp3-menu-item{
  background:none;
  border:none;
  text-align:left;
  width:100%; }
.bp3-menu-header{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px;
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    line-height:17px;
    margin:0;
    padding:10px 7px 0 1px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    font-size:18px;
    padding-bottom:5px;
    padding-top:15px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item{ }
  .bp3-dark .bp3-menu-item.bp3-intent-primary{
    color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-success{
    color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning{
    color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger{
    color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item::before,
  .bp3-dark .bp3-menu-item > .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item .bp3-menu-item-label{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
    background-color:rgba(138, 155, 168, 0.3); }
  .bp3-dark .bp3-menu-item.bp3-disabled{
    color:rgba(167, 182, 194, 0.6) !important; }
    .bp3-dark .bp3-menu-item.bp3-disabled::before,
    .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  background-color:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  height:50px;
  padding:0 15px;
  position:relative;
  width:100%;
  z-index:10; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    left:0;
    position:fixed;
    right:0;
    top:0; }

.bp3-navbar-heading{
  font-size:16px;
  margin-right:15px; }

.bp3-navbar-group{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px;
  margin:0 10px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:100%;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  text-align:center;
  width:100%; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  bottom:0;
  left:0;
  position:static;
  right:0;
  top:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    overflow:hidden;
    position:fixed; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    overflow:auto;
    position:fixed; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  bottom:0;
  left:0;
  position:fixed;
  right:0;
  top:0;
  opacity:1;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  z-index:20; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }
  .bp3-panel-stack-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-panel-stack2{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack2-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack2-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack2-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack2-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack2-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack2-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-view{
    background-color:#30404d; }
  .bp3-panel-stack2-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter, .bp3-panel-stack2-push .bp3-panel-stack2-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter-active, .bp3-panel-stack2-push .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter, .bp3-panel-stack2-pop .bp3-panel-stack2-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter-active, .bp3-panel-stack2-pop .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  border-radius:3px;
  display:inline-block;
  z-index:20; }
  .bp3-popover .bp3-popover-arrow{
    height:30px;
    position:absolute;
    width:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      height:20px;
      margin:5px;
      width:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-bottom:17px;
    margin-top:-17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-left:-17px;
    margin-right:17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover .bp3-popover-content{
    border-radius:3px;
    position:relative; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  border-radius:2px;
  content:"";
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg); }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  left:0;
  position:absolute;
  right:0;
  top:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  background:rgba(92, 112, 128, 0.2);
  border-radius:40px;
  display:block;
  height:8px;
  overflow:hidden;
  position:relative;
  width:100%; }
  .bp3-progress-bar .bp3-progress-meter{
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    border-radius:40px;
    height:100%;
    position:absolute;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:100%; }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  color:transparent !important;
  cursor:default;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  height:40px;
  min-width:150px;
  width:100%;
  cursor:default;
  outline:none;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    cursor:not-allowed;
    opacity:0.5; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  height:6px;
  left:0;
  right:0;
  top:5px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  height:16px;
  left:0;
  position:absolute;
  top:0;
  width:16px; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab;
    z-index:2; }
  .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    background:#bfccd6;
    -webkit-box-shadow:none;
            box-shadow:none;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    background:#5c7080;
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-slider-handle .bp3-slider-label{
    background:#394b59;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    color:#f5f8fa;
    margin-left:8px; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      background:#e1e8ed;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-bottom-right-radius:0;
    border-top-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    border-bottom-left-radius:0;
    border-top-left-radius:0;
    margin-left:8px; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  font-size:12px;
  line-height:1;
  padding:2px 5px;
  position:absolute;
  vertical-align:top; }

.bp3-slider.bp3-vertical{
  height:150px;
  min-width:40px;
  width:40px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    bottom:0;
    height:auto;
    left:5px;
    top:0;
    width:6px; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-left:0;
      margin-top:-8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      height:8px;
      margin-left:0;
      width:16px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-bottom-right-radius:3px;
      border-top-left-radius:0; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      border-bottom-left-radius:0;
      border-bottom-right-radius:0;
      border-top-left-radius:3px;
      margin-bottom:8px; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round;
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      padding:0 10px;
      width:100%; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        background-color:rgba(19, 124, 189, 0.2);
        -webkit-box-shadow:none;
                box-shadow:none; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      background-color:rgba(19, 124, 189, 0.2);
      border-radius:3px;
      bottom:0;
      height:auto;
      left:0;
      right:0;
      top:0; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  border:none;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  list-style:none;
  margin:0;
  padding:0;
  position:relative; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:#182026;
  cursor:pointer;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  font-size:14px;
  line-height:30px;
  max-width:100%;
  position:relative;
  vertical-align:top; }
  .bp3-tab a{
    color:inherit;
    display:block;
    text-decoration:none; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    background-color:transparent !important;
    -webkit-box-shadow:none !important;
            box-shadow:none !important; }
  .bp3-tab[aria-disabled="true"]{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    font-size:16px;
    line-height:40px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  left:0;
  pointer-events:none;
  position:absolute;
  top:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    background-color:#106ba3;
    bottom:0;
    height:3px;
    left:0;
    position:absolute;
    right:0; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#5c7080;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  color:#f5f8fa;
  font-size:12px;
  line-height:16px;
  max-width:100%;
  min-height:20px;
  min-width:20px;
  padding:2px 6px;
  position:relative; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-left:8px;
    padding-right:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    font-size:14px;
    line-height:20px;
    min-height:30px;
    min-width:30px;
    padding:5px 10px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-left:12px;
      padding-right:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  background:none;
  border:none;
  color:inherit;
  cursor:pointer;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin-bottom:-2px;
  margin-right:-6px !important;
  margin-top:-2px;
  opacity:0.5;
  padding:2px;
  padding-left:0; }
  .bp3-tag-remove:hover{
    background:none;
    opacity:0.8;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:0 5px 0 0; }
    .bp3-large .bp3-tag-remove:empty::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  line-height:inherit;
  min-height:30px;
  padding-left:5px;
  padding-right:0; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    color:#5c7080;
    margin-left:2px;
    margin-right:7px;
    margin-top:7px; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    margin-right:7px;
    margin-top:5px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:20px;
    width:80px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-left:5px;
      margin-top:10px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-height:30px;
      min-width:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:20px 0 0;
  max-width:500px;
  min-width:300px;
  pointer-events:all;
  position:relative !important; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-delay:50ms;
            transition-delay:50ms;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    color:#5c7080;
    margin:12px;
    margin-right:0; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    background-color:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  left:0;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none;
  right:0;
  z-index:40; }
  .bp3-toast-container.bp3-toast-container-in-portal{
    position:fixed; }
  .bp3-toast-container.bp3-toast-container-inline{
    position:absolute; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0; }
  .bp3-toast-container.bp3-toast-container-bottom{
    bottom:0;
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-exit-active ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    height:22px;
    position:absolute;
    width:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      height:14px;
      margin:4px;
      width:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-bottom:11px;
    margin-top:-11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-left:-11px;
    margin-right:11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  list-style:none;
  margin:0;
  padding-left:0; }

.bp3-tree-root{
  background-color:transparent;
  cursor:default;
  padding-left:0;
  position:relative; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:30px;
  padding-right:5px;
  width:100%; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  cursor:pointer;
  padding:7px;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  margin-right:7px;
  position:relative; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  left:calc(50% - 250px);
  top:20vh;
  width:500px;
  z-index:21; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar .bp3-input{
    background-color:transparent;
    border-radius:0; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    background-color:transparent;
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1pY29uLWJyYW5kMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNmZmYiPgogICAgPHBhdGggZD0iTTEwNSAxMjcuM2g0MHYxMi44aC00MHpNNTEuMSA3N0w3NCA5OS45bC0yMy4zIDIzLjMgMTAuNSAxMC41IDIzLjMtMjMuM0w5NSA5OS45IDg0LjUgODkuNCA2MS42IDY2LjV6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNGOUE4MjUiPgogICAgPHBhdGggZD0iTTIwLjIgMTEuOGMtMS42IDAtMS43LjUtMS43IDEgMCAuNC4xLjkuMSAxLjMuMS41LjEuOS4xIDEuMyAwIDEuNy0xLjQgMi4zLTMuNSAyLjNoLS45di0xLjloLjVjMS4xIDAgMS40IDAgMS40LS44IDAtLjMgMC0uNi0uMS0xIDAtLjQtLjEtLjgtLjEtMS4yIDAtMS4zIDAtMS44IDEuMy0yLTEuMy0uMi0xLjMtLjctMS4zLTIgMC0uNC4xLS44LjEtMS4yLjEtLjQuMS0uNy4xLTEgMC0uOC0uNC0uNy0xLjQtLjhoLS41VjQuMWguOWMyLjIgMCAzLjUuNyAzLjUgMi4zIDAgLjQtLjEuOS0uMSAxLjMtLjEuNS0uMS45LS4xIDEuMyAwIC41LjIgMSAxLjcgMXYxLjh6TTEuOCAxMC4xYzEuNiAwIDEuNy0uNSAxLjctMSAwLS40LS4xLS45LS4xLTEuMy0uMS0uNS0uMS0uOS0uMS0xLjMgMC0xLjYgMS40LTIuMyAzLjUtMi4zaC45djEuOWgtLjVjLTEgMC0xLjQgMC0xLjQuOCAwIC4zIDAgLjYuMSAxIDAgLjIuMS42LjEgMSAwIDEuMyAwIDEuOC0xLjMgMkM2IDExLjIgNiAxMS43IDYgMTNjMCAuNC0uMS44LS4xIDEuMi0uMS4zLS4xLjctLjEgMSAwIC44LjMuOCAxLjQuOGguNXYxLjloLS45Yy0yLjEgMC0zLjUtLjYtMy41LTIuMyAwLS40LjEtLjkuMS0xLjMuMS0uNS4xLS45LjEtMS4zIDAtLjUtLjItMS0xLjctMXYtMS45eiIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSIxMy44IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY3g9IjExIiBjeT0iOC4yIiByPSIyLjEiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgPGcgY2xhc3M9ImpwLWljb24td2FybjAiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4=);
  --jp-icon-listings-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MC45NzggNTAuOTc4IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MC45NzggNTAuOTc4OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8Zz4KCQk8cGF0aCBzdHlsZT0iZmlsbDojMDEwMDAyOyIgZD0iTTQzLjUyLDcuNDU4QzM4LjcxMSwyLjY0OCwzMi4zMDcsMCwyNS40ODksMEMxOC42NywwLDEyLjI2NiwyLjY0OCw3LjQ1OCw3LjQ1OAoJCQljLTkuOTQzLDkuOTQxLTkuOTQzLDI2LjExOSwwLDM2LjA2MmM0LjgwOSw0LjgwOSwxMS4yMTIsNy40NTYsMTguMDMxLDcuNDU4YzAsMCwwLjAwMSwwLDAuMDAyLDAKCQkJYzYuODE2LDAsMTMuMjIxLTIuNjQ4LDE4LjAyOS03LjQ1OGM0LjgwOS00LjgwOSw3LjQ1Ny0xMS4yMTIsNy40NTctMTguMDNDNTAuOTc3LDE4LjY3LDQ4LjMyOCwxMi4yNjYsNDMuNTIsNy40NTh6CgkJCSBNNDIuMTA2LDQyLjEwNWMtNC40MzIsNC40MzEtMTAuMzMyLDYuODcyLTE2LjYxNSw2Ljg3MmgtMC4wMDJjLTYuMjg1LTAuMDAxLTEyLjE4Ny0yLjQ0MS0xNi42MTctNi44NzIKCQkJYy05LjE2Mi05LjE2My05LjE2Mi0yNC4wNzEsMC0zMy4yMzNDMTMuMzAzLDQuNDQsMTkuMjA0LDIsMjUuNDg5LDJjNi4yODQsMCwxMi4xODYsMi40NCwxNi42MTcsNi44NzIKCQkJYzQuNDMxLDQuNDMxLDYuODcxLDEwLjMzMiw2Ljg3MSwxNi42MTdDNDguOTc3LDMxLjc3Miw0Ni41MzYsMzcuNjc1LDQyLjEwNiw0Mi4xMDV6Ii8+CgkJPHBhdGggc3R5bGU9ImZpbGw6IzAxMDAwMjsiIGQ9Ik0yMy41NzgsMzIuMjE4Yy0wLjAyMy0xLjczNCwwLjE0My0zLjA1OSwwLjQ5Ni0zLjk3MmMwLjM1My0wLjkxMywxLjExLTEuOTk3LDIuMjcyLTMuMjUzCgkJCWMwLjQ2OC0wLjUzNiwwLjkyMy0xLjA2MiwxLjM2Ny0xLjU3NWMwLjYyNi0wLjc1MywxLjEwNC0xLjQ3OCwxLjQzNi0yLjE3NWMwLjMzMS0wLjcwNywwLjQ5NS0xLjU0MSwwLjQ5NS0yLjUKCQkJYzAtMS4wOTYtMC4yNi0yLjA4OC0wLjc3OS0yLjk3OWMtMC41NjUtMC44NzktMS41MDEtMS4zMzYtMi44MDYtMS4zNjljLTEuODAyLDAuMDU3LTIuOTg1LDAuNjY3LTMuNTUsMS44MzIKCQkJYy0wLjMwMSwwLjUzNS0wLjUwMywxLjE0MS0wLjYwNywxLjgxNGMtMC4xMzksMC43MDctMC4yMDcsMS40MzItMC4yMDcsMi4xNzRoLTIuOTM3Yy0wLjA5MS0yLjIwOCwwLjQwNy00LjExNCwxLjQ5My01LjcxOQoJCQljMS4wNjItMS42NCwyLjg1NS0yLjQ4MSw1LjM3OC0yLjUyN2MyLjE2LDAuMDIzLDMuODc0LDAuNjA4LDUuMTQxLDEuNzU4YzEuMjc4LDEuMTYsMS45MjksMi43NjQsMS45NSw0LjgxMQoJCQljMCwxLjE0Mi0wLjEzNywyLjExMS0wLjQxLDIuOTExYy0wLjMwOSwwLjg0NS0wLjczMSwxLjU5My0xLjI2OCwyLjI0M2MtMC40OTIsMC42NS0xLjA2OCwxLjMxOC0xLjczLDIuMDAyCgkJCWMtMC42NSwwLjY5Ny0xLjMxMywxLjQ3OS0xLjk4NywyLjM0NmMtMC4yMzksMC4zNzctMC40MjksMC43NzctMC41NjUsMS4xOTljLTAuMTYsMC45NTktMC4yMTcsMS45NTEtMC4xNzEsMi45NzkKCQkJQzI2LjU4OSwzMi4yMTgsMjMuNTc4LDMyLjIxOCwyMy41NzgsMzIuMjE4eiBNMjMuNTc4LDM4LjIydi0zLjQ4NGgzLjA3NnYzLjQ4NEgyMy41Nzh6Ii8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMEQ0N0ExIj4KICAgIDxwYXRoIGQ9Ik0xMS4xIDYuOVY1LjhINi45YzAtLjUgMC0xLjMuMi0xLjYuNC0uNy44LTEuMSAxLjctMS40IDEuNy0uMyAyLjUtLjMgMy45LS4xIDEgLjEgMS45LjkgMS45IDEuOXY0LjJjMCAuNS0uOSAxLjYtMiAxLjZIOC44Yy0xLjUgMC0yLjQgMS40LTIuNCAyLjh2Mi4ySDQuN0MzLjUgMTUuMSAzIDE0IDMgMTMuMVY5Yy0uMS0xIC42LTIgMS44LTIgMS41LS4xIDYuMy0uMSA2LjMtLjF6Ii8+CiAgICA8cGF0aCBkPSJNMTAuOSAxNS4xdjEuMWg0LjJjMCAuNSAwIDEuMy0uMiAxLjYtLjQuNy0uOCAxLjEtMS43IDEuNC0xLjcuMy0yLjUuMy0zLjkuMS0xLS4xLTEuOS0uOS0xLjktMS45di00LjJjMC0uNS45LTEuNiAyLTEuNmgzLjhjMS41IDAgMi40LTEuNCAyLjQtMi44VjYuNmgxLjdDMTguNSA2LjkgMTkgOCAxOSA4LjlWMTNjMCAxLS43IDIuMS0xLjkgMi4xaC02LjJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMikiIGZpbGw9IiMzMzMzMzMiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uLWFjY2VudDIganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGQ9Ik01LjA1NjY0IDguNzYxNzJDNS4wNTY2NCA4LjU5NzY2IDUuMDMxMjUgOC40NTMxMiA0Ljk4MDQ3IDguMzI4MTJDNC45MzM1OSA4LjE5OTIyIDQuODU1NDcgOC4wODIwMyA0Ljc0NjA5IDcuOTc2NTZDNC42NDA2MiA3Ljg3MTA5IDQuNSA3Ljc3NTM5IDQuMzI0MjIgNy42ODk0NUM0LjE1MjM0IDcuNTk5NjEgMy45NDMzNiA3LjUxMTcyIDMuNjk3MjcgNy40MjU3OEMzLjMwMjczIDcuMjg1MTYgMi45NDMzNiA3LjEzNjcyIDIuNjE5MTQgNi45ODA0N0MyLjI5NDkyIDYuODI0MjIgMi4wMTc1OCA2LjY0MjU4IDEuNzg3MTEgNi40MzU1NUMxLjU2MDU1IDYuMjI4NTIgMS4zODQ3NyA1Ljk4ODI4IDEuMjU5NzcgNS43MTQ4NEMxLjEzNDc3IDUuNDM3NSAxLjA3MjI3IDUuMTA5MzggMS4wNzIyNyA0LjczMDQ3QzEuMDcyMjcgNC4zOTg0NCAxLjEyODkxIDQuMDk1NyAxLjI0MjE5IDMuODIyMjdDMS4zNTU0NyAzLjU0NDkyIDEuNTE1NjIgMy4zMDQ2OSAxLjcyMjY2IDMuMTAxNTZDMS45Mjk2OSAyLjg5ODQ0IDIuMTc5NjkgMi43MzQzNyAyLjQ3MjY2IDIuNjA5MzhDMi43NjU2MiAyLjQ4NDM4IDMuMDkxOCAyLjQwNDMgMy40NTExNyAyLjM2OTE0VjEuMTA5MzhINC4zODg2N1YyLjM4MDg2QzQuNzQwMjMgMi40Mjc3MyA1LjA1NjY0IDIuNTIzNDQgNS4zMzc4OSAyLjY2Nzk3QzUuNjE5MTQgMi44MTI1IDUuODU3NDIgMy4wMDE5NSA2LjA1MjczIDMuMjM2MzNDNi4yNTE5NSAzLjQ2NjggNi40MDQzIDMuNzQwMjMgNi41MDk3NyA0LjA1NjY0QzYuNjE5MTQgNC4zNjkxNCA2LjY3MzgzIDQuNzIwNyA2LjY3MzgzIDUuMTExMzNINS4wNDQ5MkM1LjA0NDkyIDQuNjM4NjcgNC45Mzc1IDQuMjgxMjUgNC43MjI2NiA0LjAzOTA2QzQuNTA3ODEgMy43OTI5NyA0LjIxNjggMy42Njk5MiAzLjg0OTYxIDMuNjY5OTJDMy42NTAzOSAzLjY2OTkyIDMuNDc2NTYgMy42OTcyNyAzLjMyODEyIDMuNzUxOTVDMy4xODM1OSAzLjgwMjczIDMuMDY0NDUgMy44NzY5NSAyLjk3MDcgMy45NzQ2MUMyLjg3Njk1IDQuMDY4MzYgMi44MDY2NCA0LjE3OTY5IDIuNzU5NzcgNC4zMDg1OUMyLjcxNjggNC40Mzc1IDIuNjk1MzEgNC41NzgxMiAyLjY5NTMxIDQuNzMwNDdDMi42OTUzMSA0Ljg4MjgxIDIuNzE2OCA1LjAxOTUzIDIuNzU5NzcgNS4xNDA2MkMyLjgwNjY0IDUuMjU3ODEgMi44ODI4MSA1LjM2NzE5IDIuOTg4MjggNS40Njg3NUMzLjA5NzY2IDUuNTcwMzEgMy4yNDAyMyA1LjY2Nzk3IDMuNDE2MDIgNS43NjE3MkMzLjU5MTggNS44NTE1NiAzLjgxMDU1IDUuOTQzMzYgNC4wNzIyNyA2LjAzNzExQzQuNDY2OCA2LjE4NTU1IDQuODI0MjIgNi4zMzk4NCA1LjE0NDUzIDYuNUM1LjQ2NDg0IDYuNjU2MjUgNS43MzgyOCA2LjgzOTg0IDUuOTY0ODQgNy4wNTA3OEM2LjE5NTMxIDcuMjU3ODEgNi4zNzEwOSA3LjUgNi40OTIxOSA3Ljc3NzM0QzYuNjE3MTkgOC4wNTA3OCA2LjY3OTY5IDguMzc1IDYuNjc5NjkgOC43NUM2LjY3OTY5IDkuMDkzNzUgNi42MjMwNSA5LjQwNDMgNi41MDk3NyA5LjY4MTY0QzYuMzk2NDggOS45NTUwOCA2LjIzNDM4IDEwLjE5MTQgNi4wMjM0NCAxMC4zOTA2QzUuODEyNSAxMC41ODk4IDUuNTU4NTkgMTAuNzUgNS4yNjE3MiAxMC44NzExQzQuOTY0ODQgMTAuOTg4MyA0LjYzMjgxIDExLjA2NDUgNC4yNjU2MiAxMS4wOTk2VjEyLjI0OEgzLjMzMzk4VjExLjA5OTZDMy4wMDE5NSAxMS4wNjg0IDIuNjc5NjkgMTAuOTk2MSAyLjM2NzE5IDEwLjg4MjhDMi4wNTQ2OSAxMC43NjU2IDEuNzc3MzQgMTAuNTk3NyAxLjUzNTE2IDEwLjM3ODlDMS4yOTY4OCAxMC4xNjAyIDEuMTA1NDcgOS44ODQ3NyAwLjk2MDkzOCA5LjU1MjczQzAuODE2NDA2IDkuMjE2OCAwLjc0NDE0MSA4LjgxNDQ1IDAuNzQ0MTQxIDguMzQ1N0gyLjM3ODkxQzIuMzc4OTEgOC42MjY5NSAyLjQxOTkyIDguODYzMjggMi41MDE5NSA5LjA1NDY5QzIuNTgzOTggOS4yNDIxOSAyLjY4OTQ1IDkuMzkyNTggMi44MTgzNiA5LjUwNTg2QzIuOTUxMTcgOS42MTUyMyAzLjEwMTU2IDkuNjkzMzYgMy4yNjk1MyA5Ljc0MDIzQzMuNDM3NSA5Ljc4NzExIDMuNjA5MzggOS44MTA1NSAzLjc4NTE2IDkuODEwNTVDNC4yMDMxMiA5LjgxMDU1IDQuNTE5NTMgOS43MTI4OSA0LjczNDM4IDkuNTE3NThDNC45NDkyMiA5LjMyMjI3IDUuMDU2NjQgOS4wNzAzMSA1LjA1NjY0IDguNzYxNzJaTTEzLjQxOCAxMi4yNzE1SDguMDc0MjJWMTFIMTMuNDE4VjEyLjI3MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzLjk1MjY0IDYpIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTUgMTVIM3YyaDEydi0yem0wLThIM3YyaDEyVjd6TTMgMTNoMTh2LTJIM3Yyem0wIDhoMTh2LTJIM3Yyek0zIDN2MmgxOFYzSDN6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}
.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}
.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}
.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-border-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0px;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-warn-color0);
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px 5px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FileDialog-Checkbox {
  margin-top: 35px;
  display: flex;
  flex-direction: row;
  align-items: end;
  width: 100%;
}

.jp-FileDialog-Checkbox > label {
  flex: 1 1 auto;
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
  overflow-x: auto;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 50px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -50px; margin-right: -50px;
  padding-bottom: 50px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 50px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
  outline: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -50px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }

.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}

.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .remote-caret {
  position: relative;
  border-left: 2px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .remote-caret > div {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -2px;
  font-size: 0.95em;
  background-color: rgb(250, 129, 0);
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 3;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .remote-caret.hide-name > div {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .remote-caret:hover > div {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
  margin: 8px 12px 0px 12px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: flex-start;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0px;
  padding-right: 2px;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 40px;
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent {
  width: 72px;
  background: var(--jp-brand-color1);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent:focus-visible {
  background-color: var(--jp-brand-color0);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent
  .jp-icon3 {
  fill: white;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileBrowser-filterBox {
  padding: 0px;
  flex: 0 0 auto;
  margin: 8px 12px 0px 12px;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing:focus-visible {
  border: 1px solid var(--jp-brand-color1);
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon:before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

body[data-format='mobile'] .jp-OutputArea-child {
  flex-direction: column;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-OutputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  margin-left: var(--jp-notebook-padding);
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
  overflow: hidden;
}

body[data-format='mobile'] .jp-InputArea {
  flex-direction: column;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
  overflow: hidden;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

body[data-format='mobile'] .jp-InputArea-editor {
  margin-left: var(--jp-notebook-padding);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-InputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

.jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
}

.jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-collapseHeadingButton {
  display: none;
}

.jp-MarkdownCell:hover .jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook-render * {
  contain: none !important;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
  float: left;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt:before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body div {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>

    <style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0px 2px 1px -1px var(--jp-shadow-umbra-color),
    0px 1px 1px 0px var(--jp-shadow-penumbra-color),
    0px 1px 3px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0px 3px 1px -2px var(--jp-shadow-umbra-color),
    0px 2px 2px 0px var(--jp-shadow-penumbra-color),
    0px 1px 5px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0px 2px 4px -1px var(--jp-shadow-umbra-color),
    0px 4px 5px 0px var(--jp-shadow-penumbra-color),
    0px 1px 10px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0px 3px 5px -1px var(--jp-shadow-umbra-color),
    0px 6px 10px 0px var(--jp-shadow-penumbra-color),
    0px 1px 18px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0px 5px 5px -3px var(--jp-shadow-umbra-color),
    0px 8px 10px 1px var(--jp-shadow-penumbra-color),
    0px 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0px 7px 8px -4px var(--jp-shadow-umbra-color),
    0px 12px 17px 2px var(--jp-shadow-penumbra-color),
    0px 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0px 8px 10px -5px var(--jp-shadow-umbra-color),
    0px 16px 24px 2px var(--jp-shadow-penumbra-color),
    0px 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0px 10px 13px -6px var(--jp-shadow-umbra-color),
    0px 20px 31px 3px var(--jp-shadow-penumbra-color),
    0px 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0px 11px 15px -7px var(--jp-shadow-umbra-color),
    0px 24px 38px 3px var(--jp-shadow-penumbra-color),
    0px 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;

  --jp-ui-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;

  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);

  --jp-content-link-color: var(--md-blue-700);

  --jp-content-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);

  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;

  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;

  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);

  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-border-color1);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: #05a;
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #aa22ff;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #aa22ff;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);
}
</style>

<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

.highlight  {
  margin: 0.4em;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.CodeMirror pre {
  margin: 0;
  padding: 0;
}

/* Using table instead of flexbox so that we can use break-inside property */
/* CSS rules under this comment should not be required anymore after we move to the JupyterLab 4.0 CSS */


.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  min-width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-OutputArea-child {
  display: table;
  width: 100%;
}

.jp-OutputPrompt {
  display: table-cell;
  vertical-align: top;
  min-width: var(--jp-cell-prompt-width);
}

body[data-format='mobile'] .jp-OutputPrompt {
  display: table-row;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  display: table-row;
}

.jp-OutputArea-output.jp-OutputArea-executeResult {
  width: 100%;
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }

  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}
</style>

<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: { 
                    automatic: true 
                    }
                }
            });
        
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
    <!-- End of mathjax configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<ul>
<li>A Random process could be thought of as a collection of indexed random variables (i.e., a vector) that <strong>evolves in time</strong> .</li>
<li>Each RV (element) in a collection (vector) follows a specific distribution.</li>
<li>If all RVs in a collection have the same distribution and are independent of each other then we call it i.i.d(Independent and Identically distributed). Ex: Bernoulli Process</li>
<li>Often, Gaussian distribution for RVs is assumed.</li>
<li><strong>Then what is the difference between observing an outcome of a random variable, which forms a sequence, and a random process?</strong> 
  <br> The outcome of a random process is a function (of time) whereas the outcome of a RV is a number.</li>
<li>A set of all possible values of  RVs is called <strong>state space (S)</strong>, and one single observation is <strong>sample function</strong> or <strong>realization</strong>.</li>
<li>If both state space (S) and time (T) is discrete then we call it a <strong>discrete random sequence.</strong> (Ex, Sequence of Coin toss, $X_n,n \geq 1,$ and $S=\{0,1\}$.</li>
<li><strong>Continuous Random sequence</strong> ($S \in \mathbb{R}, T \in \mathbb{Z}$), Ex: Temperature or pressure variation observed in discrete instant of time.</li>
<li><strong>Discrete Random Process</strong> ($S \in \mathbb{Z}, T \in \mathbb{R}$), Ex: Number of packets received over a time interval</li>
<li><strong>Continuous Random Process</strong> ($S \in \mathbb{R}, T \in \mathbb{R}$), Ex: Temperature or pressure variation observed over an inetrval.</li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">scipy</span> <span class="kn">import</span> <span class="n">signal</span> <span class="k">as</span> <span class="n">sig</span>
<span class="kn">from</span> <span class="nn">matplotlib</span> <span class="kn">import</span> <span class="n">pyplot</span> <span class="k">as</span> <span class="n">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">style</span><span class="o">.</span><span class="n">use</span><span class="p">(</span><span class="s1">&#39;ggplot&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Generate a single <strong>realization</strong> of Bernoulli Process. Produce a  <strong>correlated</strong> process using a simple filter having a difference equation $$ y(n) = 0.5y(n-1)+x(n)$$ or with an equivalent system function representation $$ H(z)=\frac{1}{1-0.5z^{-1}}$$</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">,(</span><span class="mi">1</span><span class="p">,</span><span class="mi">50</span><span class="p">))</span>
<span class="n">b</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">])</span>
<span class="n">a</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span><span class="o">-</span><span class="mf">0.5</span><span class="p">])</span>
<span class="n">yn</span> <span class="o">=</span> <span class="n">sig</span><span class="o">.</span><span class="n">lfilter</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="n">a</span><span class="p">,</span><span class="n">xn</span><span class="p">)</span>
<span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">),</span><span class="n">sharex</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">xn</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">yn</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;Index&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$y(n)$&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$x(n)$&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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ze24+3ngwIEaMWKEwuEweXYZn8+nAQMGSJLa29vV3t4un8+ngwcPasqUKZKkmTNnkucU19jYqJqaGs2ePVuSFI1GybEHmN1fc70hQeFwWIFAoONxIBBQXV2djRHBTB9++KFyc3MlnS+uTp48aXNESJb6+nodPXpUV1xxBXl2oUgkonvuuUcffPCBbrzxRg0bNkyZmZlKT0+XJOXl5SkcDtscJfpi27Zt+upXv6qzZ89Kkk6dOkWOXWjdunWSpM997nMKhUKm99cUyAnqbnY8n89nQyQAEtXS0qKKigrdeuutyszMtDscmCAtLU0/+tGPdPr0aT366KP6v//7P7tDQhK9+eabysnJUUFBgQ4ePGh3ODDJQw89pLy8PH344Yf64Q9/qPz8fNP3SYGcoEAgoMbGxo7HjY2NHb9k4D45OTlqampSbm6umpqaGGvuAm1tbaqoqNANN9ygyZMnSyLPbnbJJZeoqKhIdXV1OnPmjNrb25Wenq5wOKy8vDy7w0OC3n77be3bt0+1tbU6d+6czp49q23btpFjl7mQv5ycHF1zzTU6cuSI6f01Y5ATVFhYqPfff1/19fVqa2vT66+/ruLiYrvDgkmKi4v16quvSpJeffVVXXPNNTZHhL6IRqN66qmnNGLECM2dO7djO3l2l5MnT+r06dOSzs9o8dZbb2nEiBEaN26c9uzZI0mqrq6m705hS5cu1VNPPaXKykqtWrVKn/70p7Vy5Upy7CItLS0dw2daWlp04MABjR492vT+mpX0+qCmpkY/+9nPFIlENGvWLN188812h4Qk2LBhgw4dOqRTp04pJydHixYt0jXXXKPHHntMDQ0NCgaD+ta3vsX0XynsD3/4g773ve9p9OjRHUOjlixZoiuvvJI8u8if//xnVVZWKhKJKBqNaurUqVq4cKGOHz/eZQowv99vd7joo4MHD+rFF1/UmjVryLGLHD9+XI8++qik8zfbXn/99br55pt16tQpU/trCmQAAADAgCEWAAAAgAEFMgAAAGBAgQwAAAAYUCADAAAABhTIAAAAgAEFMgC42LPPPquNGzfaHQYApBQKZABIAXfccYcOHDhgdxgA4AkUyAAAAIBBht0BAABiV11drd/85je68sor9dvf/laZmZlavny5JkyYIEmqr69XZWWljh49qiuvvFL5+fmd/v7w4cP6+c9/rvfee09DhgzRrbfeqnHjxumjjz7St7/9bS1fvlzFxcVqaWnR6tWrtXDhQs2YMcOOQwUA23AGGQBSzJEjR5Sfn68tW7boi1/8op566ildWBT18ccfV0FBgbZs2aIvfelLevXVVzv+LhwOq7y8XDfffLP++Z//WaWlpaqoqNDJkyeVlZWlb37zm3r66af14Ycfatu2bRozZgzFMQBPokAGgBQTDAYVCoWUlpamGTNmqKmpSR9++KEaGhr0xz/+UYsXL5bf71dRUZEmTZrU8Xe7d+/WhAkTNHHiRKWlpWn8+PEqLCxUTU2NJOmzn/2spk6dqh/84Aeqra3V7bffbtchAoCtGGIBAClm8ODBHf/u37+/JKmlpUUnT57UJZdcogEDBnQ8P2TIEDU0NEiSGhoatGfPHr355psdz7e3t2vcuHEdj0OhkF5++WUtWLBA2dnZZh8KADgSBTIAuERubq5Onz6tlpaWjiL5QnEsSYFAQDfccINWrFjR7d9HIhH99Kc/1fTp07Vr1y7NmjVLw4cPtyR2AHAShlgAgEsMGTJEhYWFevbZZ9XW1qY//OEPnc4W33DDDXrzzTe1f/9+RSIRnTt3TgcPHlRjY6Mk6T//8z8lSWVlZfrCF76gJ554QpFIxJZjAQA7USADgIusXLlSR44c0d/93d/pueee0/Tp0zueCwaD+s53vqPnn39ey5Yt0ze/+U398pe/VDQa1TvvvKOXXnpJf//3f6+0tDTNnz9fPp9Pv/jFL2w8GgCwhy964dZnAAAAAJxBBgAAAIwokAEAAAADCmQAAADAgAIZAAAAMKBABgAAAAwokAEAAAADCmQAAADAgAIZAAAAMPj/NZZiuv2PEAcAAAAASUVORK5CYII=
"
class="
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;The variance of the process xn is: &#39;</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">xn</span><span class="p">)</span> <span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;The variance of the process yn is: &#39;</span><span class="p">,</span><span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">yn</span><span class="p">)</span> <span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>The variance of the process xn is:  0.24857142857142858
The variance of the process yn is:  0.2681514506288874
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Ensemble-Average">Ensemble Average<a class="anchor-link" href="#Ensemble-Average">&#182;</a></h3><ul>
<li>If we have N realizations of a RP, then ensemble mean at an instant $n$ is an average obtained by summing acrosss all the realization.
$$ m_x(n) =  E\{x(n)\}$$</li>
<li>Similarly ensemble variance could be calculated for each instant of $n$ as follows $$ \sigma^2_x(n)=E\{(x(n)-m_x(n))^2\}$$</li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[170]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">m</span> <span class="o">=</span> <span class="mi">100</span> <span class="c1"># no.of realizations</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">50</span> 
<span class="n">xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">2</span><span class="p">,(</span><span class="n">N</span><span class="p">,</span><span class="n">m</span><span class="p">))</span>
<span class="n">m_xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">xn</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">sig_xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">var</span><span class="p">(</span><span class="n">xn</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[171]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">4</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">6</span><span class="p">),</span><span class="n">sharex</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">xn</span><span class="p">[:,</span><span class="mi">0</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">xn</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">m_xn</span><span class="p">,</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">sig_xn</span><span class="p">,</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$x(n)$&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Realization 1&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Realization 2&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Ensemble Mean&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Ensemble Variance&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;Index&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">([</span><span class="o">-</span><span class="mf">0.1</span><span class="p">,</span><span class="mi">2</span><span class="p">])</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA1gAAAGoCAYAAABbkkSYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzdfVxUZf7/8fcEIngPjopA3mApammam5l3WBR+1byhTTM1NS3T+tmdlVombZasK5lrtrXdqKtLZe1a+13bUiyTNI1NKBVTd9XuVBTRzRIEnPP7w6+zToICc+YcDryejwePB3PO+Zzrc11zzWE+c84cXIZhGAIAAAAA+O0SuxMAAAAAgOqCAgsAAAAATEKBBQAAAAAmocACAAAAAJNQYAEAAACASSiwAAAAAMAkFFgAgCrP5XJpxYoV3setWrXSnDlzAt6uVe0AAKoPCiwAQIWNGzdOLpdLLpdLQUFBiomJ0R133KEffvjBkvYzMzP14IMPmra/iRMnKj4+PuDtlKWwsFDjx49Xly5dFBISossuuyzgbQIAAoMCCwBQKb1799bBgwf17bffKi0tTVlZWbr11lstabtJkyaqW7dutWnn9OnTCgkJ0d13363bbrst4O0BAAKHAgsAUCkhISGKjIxUdHS0+vTpo7vvvlufffaZfvzxR5/tFi1apLi4OIWGhuryyy/XM888o5KSEu/6tLQ0de/eXQ0bNpTb7dbAgQO1e/fuC7Z97qV7S5cu9Z5NO/fn7BmpY8eOafTo0WrRooXCwsLUrl07paamyjAMSVJycrJee+01ffLJJ97YpUuXnteOJJ04cUKTJk1SkyZNFBoaqm7dumnNmjXe9fv375fL5dLKlSt18803q06dOoqNjdXy5csv2J+6devq5Zdf1uTJkxUbG3vhgQcAVGkUWAAAvx04cEDvvPOOgoKCFBQU5F2enJys+fPna+7cudq5c6cWLlyol19+WU899ZR3m1OnTmnWrFnaunWr1q5dq6CgIA0cOFBFRUXlanvEiBE6ePCg92fTpk2qX7+++vXr593/lVdeqXfffVc5OTmaNWuWZs+e7S2ipk2bpttvv109evTw7mPEiBGltnXnnXfqww8/1IoVK5SVlaWePXtq0KBB+vrrr322mz59usaMGaOvvvpKw4cP1/jx47Vnz56KDCkAwKGC7U4AAOBM69evV7169eTxeFRQUCBJevjhh72X1J08eVLz5s3TX//6V/Xv31+S1Lp1a82ZM0dTp07V008/LUkaP368z36XLl2qxo0bKzMzUz179rxoHmFhYQoLC5Mk/ec//9HEiRP1P//zP3ryySclSZGRkXrssce827du3VqZmZlKS0vT+PHjVa9ePYWFhXnPyJXlX//6l9555x2tXr1aiYmJkqSFCxcqIyND8+bN0+uvv+7d9r777tPw4cMlSXPmzNELL7ygjz76SJdffvlF+wMAcDYKLABApXTv3l3Lli1TYWGhVq5cqbVr13qLJknasWOHCgoKdMstt8jlcnmXnz59WoWFhTpy5IiaNGmi7OxsPfXUU8rOzlZeXp730r1vvvmmXAXWufsdMWKEGjRooGXLlnnb9Hg8mjdvnt588019//33KiwsVHFxsVq2bFmh/ubk5EiS+vTp47O8T58++uyzz3yWXXXVVd7fg4OD1axZM+Xm5laoPQCAM1FgAQAqJSwszHu3uyuuuEK7d+/Wvffe6z2T4/F4JElvv/222rZte158RESETp48qZtuukm9evXS66+/7j2D1LFjx3JfInjW1KlTtWvXLm3ZskWhoaHe5ampqZo7d66ee+45de3aVfXr19eCBQu0evXqSvX7lwzD8CkgpTPfTzuXy+XyjgcAoHqjwAIAmCI5OVkdO3bUlClT1K1bN3Xs2FGhoaHau3evBgwYUGrMzp07deTIET3zzDNq3769JGnTpk3es1jl9fvf/15//vOftWnTJjVt2tRn3YYNG9S/f39NmDDBu+yX34cKCQnR6dOnL9hGx44dvfs7tz8ZGRnq0qVLhfIFAFRfFFgAAFPExcVp0KBBmjFjhtauXat69epp5syZmjlzpiTpxhtvVElJibZt26asrCz99re/VcuWLVW7dm0tWrRIDz/8sPbv36/p06efd0boQtatW6eHH35Yr7/+uiIiInTo0CFJZ4qmiIgItWvXTsuXL9fHH3+s6Oho/elPf9KWLVsUHh7u3Ufr1q319ttva8eOHWrWrJnq16+v2rVr+7TTpk0b3XrrrZoyZYpefvlltWzZUn/4wx+0fft2paWl+T1+OTk5Kioq0qFDh1RUVKTs7GxJUocOHc47IwYAqLq4iyAAwDSPPvqo0tPTtW7dOknSrFmztGDBAr366qvq3Lmz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XnxERIROnjypm266Sb169dLrr7+uyMhISVLHjh3LfYngWVOnTtWuXbu0ZcsWhYaGepenpqZq7ty5eu6559S1a1fVr19fCxYs0OrVqyvV718yDMOngJTOfD/tXC6XyzseF7J9+3bdeOONGjJkiP7whz+Ykh8AwFoUWAAAUyQnJ6tjx46aMmWKunXrpo4dOyo0NFR79+7VgAEDSo3ZuXOnjhw5omeeeUbt27eXJG3atMl7Fqu8fv/73+vPf/6zNm3apKZNm/qs27Bhg/r3768JEyZ4l/3y+1AhISE6ffr0Bdvo2LGjd3/n9icjI0NdunSpUL6lyczMVP/+/TV69Gg9//zz5xVtAABn4CYXAABTxMXFadCgQZoxY4YkqV69epo5c6ZmzpypF154Qbt27dKOHTv05ptv6rHHHpMktWzZUrVr19aiRYv073//W+vWrdP9999foeJi3bp1evjhh7Vo0SJFRETo0KFDOnTokPLz8yVJ7dq10/r16/Xxxx9r9+7deuKJJ7RlyxaffbRu3Vpff/21duzYoby8vFL//1SbNm106623asqUKfrwww/19ddf6/7779f27dv1yCOPVHbYJJ0p2m644QYNGTJEM2bMUG5urrcfAABnocACAJjm0UcfVXp6utatWydJmjVrlhYsWKBXX31VnTt3Vq9evbRgwQK1atVKkuR2u7VixQqtXbtWHTt21LRp0zR//nxdckn5/zxlZGSopKREd9xxh5o3b+79SUpK8ubQt29fDRkyRD169NCxY8c0depUn31MmDBBv/rVr3TdddepSZMmeuONN0pt69VXX1ViYqJGjx6tzp07a+PGjfr73/+uuLi4SozWf73++us6ceKElixZ4tOH5s2b+7VfAID1XEZFr8MAAAAAAJSKM1gAAAAAYBJLb3KRl5enxYsX6/jx43K5XEpISCjzi88AAAAA4DSWFlhBQUEaM2aMYmNjVVBQoOnTp6tTp06KiYmxMg0AAAAACAhLLxEMDw9XbGyspDP/PyU6Otp7lycAAAAAcDrb/g/W4cOHtW/fPu8/qTxXenq60tPTJUkpKSlWpwYAAAAAlWLLXQQLCws1e/ZsJSUlqXv37hfd/sCBAxZkVT5ut1t5eXl2p4FqiLmFQGBeIRCYVwgU5hYCIVDzKioqqtTllt9FsKSkRKmpqerdu3e5iisAAAAAcApLCyzD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NLGxsXangGqKuYVAYF4hEJhXCBTmFgLBynll6U0uAAAAAKA64xJBAAAAADAJBRYAAAAAmIQCCwAAAABMQoEFAAAAACahwAIAAAAAk1BgAQAAAIBJKLAAAAAAwCQUWAAAAABgEgosAAAAADAJBRYAAAAAmIQCCwBQLaxfv14ul0vff/99mdvs379fLpdLn376qYWZAQBqEgosAIAkady4cXK5XOf91KtXz+7Uqpzk5GS5XC5dffXV56378ssvvWN3oWIPAFA9UWABALx69+6tgwcP+vzs3bvX7rSqpCZNmmjnzp3aunWrz/KXX35ZLVu2tCkrAIDdKLAAAF4hISGKjIz0+WnatKl3fXx8vCZOnKinn35akZGRioiI0Lhx4/Tzzz97t9mxY4cSExPVqFEj1a1bV+3bt9fy5cu963/66Sfdf//9io6OVp06ddSlSxf99a9/9a4/exlfWlqaEhMTVadOHcXFxemTTz7RDz/8oAEDBqhu3brq0KGDMjIyzutDVlaWrrnmGoWGhqpjx45au3btBfucm5urcePGqUmTJqpfv7569uypDRs2XHSsGjRooF//+td65ZVXvMtOnjyptLQ0TZgw4bzt//Wvf+mWW25Ro0aNFB4erptuuknbtm3zrj927JhGjx6tFi1aKCwsTO3atVNqaqoMw/BuM27cOCUkJOiPf/yjWrZsqQYNGmjIkCE6cuTIRfMFAFiDAgsAUCHvvPOO8vPztX79eqWlpendd9/VvHnzvOtHjhypxo0ba9OmTdq2bZuee+45hYeHS5IMw9DNN9+sL7/8Um+99Za2b9+uyZMn67bbbtO6det82pk1a5YmT56s7OxstW/fXiNHjtTYsWN11113KSsrS+3bt9ftt9+u4uJin7iHHnpITz75pLKysnTttddq8ODB+uGHH0rtS0FBgfr166cTJ07oH//4h7KysjRgwADdeOON2rlz50XH4u6771ZaWpq3wHzzzTfVvHlz9e7d22e73Nxc9erVS02bNlVGRoY2b96sdu3aKT4+3lscnTp1SldeeaXeffdd5eTkaNasWZo9e7aWLl3qs6/MzEx9/PHHWr16tT744ANlZ2dr2rRpF80VAGARAwAAwzDGjh1rBAUFGXXr1vX5GTRokHebvn37GldeeaVP3KRJk4xrr73W+7hBgwbGkiVLSm3j448/NmrXrm0cP37cZ/n48eONIUOGGIZhGPv27TMkGQsWLPCu//zzzw1Jxvz5873Ltm7dakgytm3b5t23JOPVV1/1blNcXGy0aNHCePzxx332nZGRYRiGYSxZssSIjo42iouLffLp16+fcf/995c5VrNnzzbatGljGIZhdOjQwXj99dcNwzCM7t27G6mpqd5cvvvuO+/23bt399mHx+MxYmNjffr5S1OnTjUSEhK8j8eOHWu43W6jsLDQu2zu3LlGZGRkmfsAAFgr2M7iDgBQtXTv3l3Lli3zWVanTh2fx1dddZXP4+joaK1Zs8b7eNq0aZo4caKWLl2q+Ph4DR48WF27dpV05uxLUVGRoqOjffZRVFSkyy+/3GdZ586dvb9HRkZKkjp16nTessOHD/vE9ejRw/t7cHCwrrnmGuXk5JTa38zMTB06dEiNGjXyWX7q1CmFhYWVGvNLd911l1555RVdffXVys7O1t///ndt3779vHa++OKL824YUlBQoD179kiSPB6P5s2bpzfffFPff/+9CgsLVVxcfN73udq3b6/atWt7H0dHRys3N7dcuQIAAo8CCwDgFRYWpssuu+yC24SEhPg8drlc8ng83sezZs3SqFGj9MEHH+ijjz7Ss88+q0cffVRz5syRx+NRw4YNlZmZedH91qpVy6eNspad23ZpjHO+w/RLHo9H7du316pVq85b98vCsixjx47VjBkz9OCDD2rYsGFyu92ltnPDDTfohRdeOG9dw4YNJUmpqamaO3eunnvuOXXt2lX169fXggULtHr1ap/tSxv/C/URAGAtCiwAgOliY2M1ZcoUTZkyRSkpKfrd736nOXPmqFu3bjp+/LgKCwt1xRVXBKTtzZs3q0OHDpKkkpISZWZmavTo0aVu261bN/3pT39SgwYNfG7mURHh4eH69a9/rRUrVpz3PbJz21m6dKmio6PLPDO2YcMG9e/f3+cGGWfPbgEAnIObXAAAvIqKinTo0KHzfsp7huSnn37Svffeq48++kj79u1TVlaWPvjgA2/Bc/311yshIUFJSUlatWqV9u7dqy+++EKLFi3yuRufP1JSUvT+++9r586dmjx5snJzczV58uRStx01apRat26tgQMHas2aNdq/f7+2bNmiuXPn6t133y13m6+88oqOHDmi66+/vtT19913n06fPq2hQ4cqIyND+/fv16effqrHH39cmzZt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hAILAAAAAExCgQUAAAAAJqHAAgAAAACTUGABAAAAgEkosAAAVdL69evlcrn0/fffl7nN/v375XK59Omnn1qYWcWVlJTI5XLpzTfftDsVAECAUWABQDU1btw4uVyu837q1atnd2pVyv3336/o6GiVlJSUur5Tp04aPXq0X20EBwfr4MGDGjp0qF/7AQBUfRRYAFCN9e7dWwcPHvT52bt3r91pVSmTJk3SgQMHtHr16vPWbd68Wdu2bdPdd99d6f0XFRVJkiIjIxUaGlrp/QAAnIECCwCqsZCQEEVGRvr8NG3a1Ls+Pj5eEydO1NNPP63IyEhFRERo3Lhx+vnnn73b7NixQ4mJiWrUqJHq1q2r9u3ba/ny5d71P/30k/csUJ06ddSlSxf99a9/9a4/exlfWlqaEhMTVadOHcXFxemTTz7RDz/8oAEDBqhu3brq0KGDMjIyzutDVlaWrrnmGoWGhqpjx45au3btBfucm5urcePGqUmTJqpfv7569uypDRs2lLl9hw4d1KtXL73yyivnrXvllVfUrl079enTR5L0wQcfqG/fvoqIiFCjRo0UHx+vf/7zn97tz14K+MILL+i2225TgwYNdMcdd5R6ieCCBQvUuXNn1atXT82bN9ftt9+uQ4cOedenp6fL5XJp3bp16tWrl8LCwnTFFVcoPT291P42bdpUoaGhiouL07Jly7zrd+/erWHDhqlRo0YKDw9XYmKiduzYccExBABUHgUWANRw77zzjvLz87V+/XqlpaXp3Xff1bx587zrR44cqcaNG2vTpk3atm2bnnvuOYWHh0uSDMPQzTffrC+//FJvvfWWtm/frsmTJ+u2227TunXrfNqZNWuWJk+erOzsbLVv314jR47U2LFjdddddykrK0vt27fX7bffruLiYp+4hx56SE8++aSysrJ07bXXavDgwfrhhx9K7UtBQYH69eunEydO6B//+IeysrI0YMAA3Xjjjdq5c2eZYzBp0iR98MEHPt/3OnHihN566y2fs1c///yz/t//+3/avHmzNm7cqNatW6t///46duyYz/6Sk5PVu3dvZWVl6emnny6z3eeee07btm3TX/7yF+3du1ejRo06b5tp06bpySef1JdffqnOnTtr+PDh+vHHH7359OnTR9u3b9cbb7yhnJwcLVy4UGFhYZKkgwcPqlevXoqOjlZGRoY+++wz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
"
class="
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Auto-Covariance">Auto-Covariance<a class="anchor-link" href="#Auto-Covariance">&#182;</a></h3><ul>
<li><p>Often, Knowing the functional representation of the process helps us to calculate the covariance of the process (Say, Harmonic process).</p>
</li>
<li><p>Since a RP is a collection of RVs, we could calculate the covariance betwenn random variables exactly as we did for two RVs.</p>
</li>
<li><p>If  sample realizations are stacked as a row in a matrix,then $n^{th}$ column represents a distribution of RV at instant $n$</p>
</li>
<li><p>$C_x(k,l) = E\{ (x(k)-m_x(k))(x(l)-m_x(l)) \} = \frac{1}{M} \sum \limits_{m=0}^{M-1} (x(k)-m_x(k))(x(l)-m_x(l)) $</p>
</li>
<li><p>$\therefore, C_x(k,l)$ forms a Matrix of size $N \times N$, where $N-1$ is the length of $x_i(n)$.Ofcourse, it will be symmetric.</p>
</li>
<li><p>In the above case, we have two($M=2$) realizations with $N = 50 $.Therefore, $C_x(k,l)$ will be of size $50 \times 50$.</p>
</li>
<li><p>Remember that,  we have $M$ realizations of a RP with $N$ RVs. Therefore, $xn$ is of size $N \times M$.</p>
</li>
<li><p>Let us manually write a code to compute the covariance and then verify the result with the Numpy function np.cov <strong>(Be careful on whether to compute sample covariance or population cov when using np.cov)</strong></p>
</li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[172]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># For the sequence above, k=0 , l=0 to 49</span>
<span class="n">k</span><span class="o">=</span><span class="mi">0</span>
<span class="n">cov_0l</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">xn</span><span class="p">[:,</span><span class="mi">0</span><span class="p">])):</span>
    <span class="n">cov_0l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">((</span><span class="n">xn</span><span class="p">[</span><span class="n">k</span><span class="p">,:]</span><span class="o">-</span><span class="n">m_xn</span><span class="p">[</span><span class="n">k</span><span class="p">])</span><span class="o">*</span><span class="p">(</span><span class="n">xn</span><span class="p">[</span><span class="n">l</span><span class="p">,:]</span><span class="o">-</span><span class="n">m_xn</span><span class="p">[</span><span class="n">l</span><span class="p">]))</span><span class="o">/</span><span class="mi">100</span><span class="p">)</span> <span class="c1"># subtract mean across observations of each rv</span>
    
<span class="nb">print</span><span class="p">(</span><span class="n">cov_0l</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>[0.24839999999999995, 0.008399999999999989, 0.03379999999999999, 0.04, -0.01, -0.010799999999999992, -0.018600000000000012, -0.010799999999999997, -0.003799999999999989, -0.014600000000000016, -0.02160000000000002, -0.02539999999999999, 0.05, 0.0007999999999999941, 0.051399999999999994, -0.009399999999999993, -0.0222, 0.07000000000000002, 0.012399999999999998, 0.0013999999999999972, -0.004600000000000017, -0.0007999999999999962, -0.008399999999999994, -0.009200000000000012, -0.009200000000000014, -0.0016000000000000142, -0.026800000000000004, 0.02079999999999998, 0.002399999999999997, -0.0006000000000000033, 0.004600000000000017, 0.02379999999999999, -0.007600000000000003, -0.029200000000000014, 0.0316, 0.05980000000000001, -0.018399999999999996, 0.019800000000000005, -0.039200000000000006, 0.013000000000000003, -0.015399999999999976, -0.008399999999999993, 0.003199999999999998, -0.010799999999999992, -0.022400000000000007, -0.016800000000000002, 0.036200000000000024, 0.044600000000000015, 0.022400000000000007, 0.010799999999999997]
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[173]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">Cov_xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">xn</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;For k=0,l=0 to 49 (i.e., first row of Cov_xn):</span><span class="se">\n</span><span class="s1"> </span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span><span class="n">Cov_xn</span><span class="p">[:,</span><span class="mi">0</span><span class="p">])</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>For k=0,l=0 to 49 (i.e., first row of Cov_xn):
 
 [ 0.25090909  0.00848485  0.03414141  0.04040404 -0.01010101 -0.01090909
 -0.01878788 -0.01090909 -0.00383838 -0.01474747 -0.02181818 -0.02565657
  0.05050505  0.00080808  0.05191919 -0.00949495 -0.02242424  0.07070707
  0.01252525  0.00141414 -0.00464646 -0.00080808 -0.00848485 -0.00929293
 -0.00929293 -0.00161616 -0.02707071  0.0210101   0.00242424 -0.00060606
  0.00464646  0.0240404  -0.00767677 -0.02949495  0.03191919  0.06040404
 -0.01858586  0.02       -0.03959596  0.01313131 -0.01555556 -0.00848485
  0.00323232 -0.01090909 -0.02262626 -0.0169697   0.03656566  0.04505051
  0.02262626  0.01090909]
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[174]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Difference between cov_0l-Cov_xn[0,:] is: </span><span class="se">\n</span><span class="s1"> </span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">Cov_xn</span><span class="p">[</span><span class="mi">0</span><span class="p">,:]</span><span class="o">-</span><span class="n">cov_0l</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Difference between cov_0l-Cov_xn[0,:] is: 
 
 [2.50909091e-03 8.48484848e-05 3.41414141e-04 4.04040404e-04
 1.01010101e-04 1.09090909e-04 1.87878788e-04 1.09090909e-04
 3.83838384e-05 1.47474747e-04 2.18181818e-04 2.56565657e-04
 5.05050505e-04 8.08080808e-06 5.19191919e-04 9.49494949e-05
 2.24242424e-04 7.07070707e-04 1.25252525e-04 1.41414141e-05
 4.64646465e-05 8.08080808e-06 8.48484848e-05 9.29292929e-05
 9.29292929e-05 1.61616162e-05 2.70707071e-04 2.10101010e-04
 2.42424242e-05 6.06060606e-06 4.64646465e-05 2.40404040e-04
 7.67676768e-05 2.94949495e-04 3.19191919e-04 6.04040404e-04
 1.85858586e-04 2.00000000e-04 3.95959596e-04 1.31313131e-04
 1.55555556e-04 8.48484848e-05 3.23232323e-05 1.09090909e-04
 2.26262626e-04 1.69696970e-04 3.65656566e-04 4.50505051e-04
 2.26262626e-04 1.09090909e-04]
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Visualization</p>
<ul>
<li>Since Covariance forms a matrix, viewing it as an image would reveal the details such as symmetry</li>
</ul>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[175]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov_xn</span><span class="p">,</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov_xn</span><span class="o">.</span><span class="n">transpose</span><span class="p">(),</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Transposed&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAsgAAAF0CAYAAAA+S8/lAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzde3Rc5Xnv8d/oaskXWZLvsizJd8vYMWCnJoAN2AkNpIkPTTgrHNKQrOa2UpKSky6cnCySnkUDbUJsmjpASpednh7ahLaH0CRAYsBuik2w8QVjG98Q8t2yLNmyLFu3mfOH1gzvNs8zSMRIaOb7WYvFnkd79n73ZR6/s2c/744lEomEAAAAAEiScga6AQAAAMB7CR1kAAAAIEAHGQAAAAjQQQYAAAACdJABAACAAB1kAAAAIEAHGQAAoJcuXLigWCymf/3Xfx3opuBdRAcZAIAsEovF0v5XXV090E0EBlzeQDcAAAD0n2PHjqWmX3rpJX3sYx/TSy+9pMrKSklSbm6u+b6Ojg4VFBT0SxuBgcYVZAAAssi4ceNS/5WVlUmSRo8enYqNHj06Nd9f/uVf6vOf/7zKysq0ZMkSSdL3v/99zZ07V0OHDtWECRN0++23q6GhIbX8p59+WrFYTM8//7yuvvpqFRUVac6cOXr++edT8yQSCf3lX/6lqqurVVhYqDFjxujDH/6wurq6JEnLly/XZZddpjVr1qi6ulpDhgzRH/7hH+rgwYORbXn00Uc1Y8YMFRQUqLKyUt/5zncUj8dTf3/++ed11VVXadiwYRoxYoQuv/zySDuOHj2q22+/XaNGjdKIESN07bXXasOGDZF1/PrXv9bs2bM1ZMgQXX755fqv//qvS3EY8B5HBxkAAJgeeOABVVVV6Xe/+51+/OMfS5JycnK0cuVKvfrqq3r88ce1d+9efepTn3rLe7/+9a/rO9/5jrZv367Zs2frE5/4hFpbWyVJ//zP/6yVK1fqRz/6kfbt26dnnnlGH/zgByPvf+ONN7R69Wr9+7//u9avX6+GhgZ9/OMfT/393/7t3/TFL35Rn//857Vz50799V//tVasWKH77rtPktTe3q6PfvSjWrx4sbZt26bNmzfrW9/6loYMGSJJam1t1eLFi9Xd3a1f//rXevnll3XDDTdoyZIlOnDggCSpvr5eH/3oR3XNNddo69atuu+++/SVr3zl0u9ovPckAABAVvrtb3+bkJSoq6t7y9/Gjh2buOmmm952GRs2bEhISjQ2NiYSiUTiqaeeSkhK/PKXv0zNU1dXl5CUWLduXSKRSCS++93vJmbPnp3o7Ow0l3n33XcncnJyEvX19anY9u3bE5ISv/3tbxOJRCIxf/78xKc+9anI++6///7EsGHDEt3d3YmjR48mJCU2btxoruOhhx5K1NTUJLq7uyPxq666KnH33XcnEolE4n/+z/+ZmDp1amSexx9/PCEp8fjjj7/tvsHgxRVkAABgev/73/+W2Nq1a/XBD35QlZWVGj58uJYuXSqp52praN68eanpiooKSdKJEyckSZ/85Cd15swZVVdX67Of/awee+wxnTt3LvL+iooKTZo0KfV67ty5GjZsmHbt2iVJ2rVrlxYtWhR5z+LFi9Xa2qr6+nqNHz9et99+u6677jrdfPPN+pu/+Rvt378/Ne+mTZt08OBBjRgxQsOGDUv9t2nTJu3bty+1joULFyon583u0jXXXNPLvYfBjA4yAAAwDR06NPJ6//79+shHPqIZM2bopz/9qTZv3qzHH39cUk8RXygs6IvFYpKUuj+4urpa+/bt049//GOVlZXpnnvu0axZsyIFhL2RXG5SIpGIxP/P//k/eumll3T99dfr2WefVW1trdasWZNqy7x587Rt27bIf7t379bf/d3fpZZ38TqQHeggAwCAXvnd736nzs5OrVy5Uh/4wAc0Y8YMHT9+/B0ta8iQIbrpppv0/e9/Xzt27FBjY6N+8YtfpP5+5MgRHTp0KPV6x44dam1t1axZsyRJtbW1Wr9+fWSZ//mf/6nhw4e/5crz17/+dT3zzDO67bbb9Pd///eSpPnz52vfvn0qKyvT1KlTI/+NHz9ekjR79my9+OKLkcK/F1544R1tLwYXOsgAAKBXpk+frng8rhUrVqiurk7/9m//liqK64tHHnlE//AP/6BXXnlF9fX1+sd//EdduHAh1fmVpKKiIn3605/Wli1b9NJLL+kzn/mM5s+fr2uvvVaS9I1vfEOPPfaYHnjgAe3bt0+PPfaYvvvd7+ruu+9WTk6Odu3apW9+85t64YUXVF9frxdeeEEbN25UbW2tJOnTn/60xo0bp5tvvllr167VG2+8oRdffFH33nuvfvnLX0qS/uzP/kz19fX6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
"
class="
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p><strong>Gausiann Process</strong></p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[176]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">m</span> <span class="o">=</span> <span class="mi">100</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">50</span>
<span class="n">xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span><span class="n">scale</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="p">(</span><span class="n">N</span><span class="p">,</span><span class="n">m</span><span class="p">))</span> <span class="c1"># mean=0, covariance = correlation</span>
<span class="n">Cov_xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">xn</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[177]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov_xn</span><span class="p">,</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov_xn</span><span class="o">.</span><span class="n">transpose</span><span class="p">(),</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Transposed&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAsgAAAF0CAYAAAA+S8/lAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzdeZRU5Z3/8U/1Dg003SwNNE3T7LsbGk1UXMgk0USZnARHgyeJiU5OoiY6OqK/RM2ZMZoogiYYo/FIJjNGY5xRo5ONMYJRiSCL7DQIzU7TdLN00/RSVb8/+tT1uZ3nW3Yb7Laq3q9zPOfeL7eqnrvU16dv3e/zROLxeFwAAAAAJElZPd0AAAAA4KOEDjIAAADgoIMMAAAAOOggAwAAAA46yAAAAICDDjIAAADgoIMMAADQSSdOnFAkEtFvfvObnm4KPkR0kAEAyCCRSCTpfyNHjuzpJgI9LqenGwAAALrPvn37guW33npLl19+ud566y2Vl5dLkrKzs72va2lpUV5eXre0Eehp3EEGACCDDBkyJPivpKREkjRo0KAgNmjQoGC773//+7ruuutUUlKiiy++WJL0wAMPaNq0aSosLNSwYcM0Z84c1dTUBO//+9//XpFIRH/+85/1iU98Qr169dLUqVP15z//OdgmHo/r+9//vkaOHKn8/HwNHjxYn/nMZ9TW1iZJmjt3rqZMmaJFixZp5MiRKigo0Kc//Wnt3LkztC8///nPNX78eOXl5am8vFx33323YrFY8O9//vOfdc4556hPnz7q16+fTjvttFA79u7dqzlz5mjgwIHq16+fzjvvPL3xxhuhz/jjH/+oyZMnq6CgQKeddpr+8pe/nIzTgI84OsgAAMBr3rx5qqio0F//+lc99thjkqSsrCwtWLBA69at07PPPqstW7bo6quv/pvX3nLLLbr77ru1Zs0aTZ48WV/84hfV0NAgSfrVr36lBQsW6JFHHlFVVZX+8Ic/6JOf/GTo9Tt27NCTTz6p//7v/9aSJUtUU1OjL3zhC8G/P/fcc/rGN76h6667TuvXr9cPf/hDzZ8/X/fee68kqbm5WZdddplmzJih1atXa8WKFfrud7+rgoICSVJDQ4NmzJihaDSqP/7xj3r77bd10UUX6eKLL9a2bdskSdXV1brssst07rnnatWqVbr33nt14403nvwDjY+eOAAAyEivvfZaXFJ8+/btf/NvpaWl8UsuueR93+ONN96IS4rX1tbG4/F4/He/+11cUvzll18Ottm+fXtcUvzVV1+Nx+Px+A9+8IP45MmT462trd73vO222+JZWVnx6urqILZmzZq4pPhrr70Wj8fj8enTp8evvvrq0Ovuu+++eJ8+feLRaDS+d+/euKT4m2++6f2Mn/70p/HKysp4NBoNxc8555z4bbfdFo/H4/F/+Zd/iY8ZMya0zbPPPhuXFH/22Wff99ggdXEHGQAAeJ111ll/E1u8eLE++clPqry8XH379tXMmTMltd9tdZ166qnBcllZmSTpwIEDkqQrr7xSR44c0ciRI3XNNdfoqaeeUmNjY+j1ZWVlGjFiRLA+bdo09enTRxs2bJAkbdiwQeeff37oNTNmzFBDQ4Oqq6s1dOhQzZkzRxdccIEuvfRS/ehHP9LWrVuDbZcvX66dO3eqX79+6tOnT/Df8uXLVVVVFXzG2Wefrays97pL5557biePHlIZHWQAAOBVWFgYWt+6das++9nPavz48XrmmWe0YsUKPfvss5Lai/hcbkFfJBKRpOD54JEjR6qqqkqPPfaYSkpKdOedd2rixImhAsLOSLxvQjweD8V/+ctf6q233tKFF16o//u//9OkSZO0aNGioC2nnnqqVq9eHfpv48aN+slPfhK8X8fPQGaggwwAADrlr3/9q1pbW7VgwQJ9/OMf1/jx47V///4P9F4FBQW65JJL9MADD2jt2rWqra3VSy+9FPz7nj17tGvXrmB97dq1amho0MSJEyVJkyZN0pIlS0LvuXTpUvXt2/dv7jzfcsst+sMf/qCrrrpKjz/+uCRp+vTpqqqqUklJicaMGRP6b+jQoZKkyZMna9myZaHCv9dff/0D7S9SCx1kAADQKePGjVMsFtP8+fO1fft2Pffcc0FRXFf87Gc/0xNPPKF33nlH1dXV+o//+A+dOHEi6PxKUq9evfTlL39ZK1eu1FtvvaWvfvWrmj59us477zxJ0u23366nnnpK8+bNU1VVlZ566in94Ac/0G233aasrCxt2LBBd9xxh15//XVVV1fr9ddf15tvvqlJkyZJkr785S9ryJAhuvTSS7V48WLt2LFDy5Yt07//+7/r5ZdfliRdf/31qq6u1re+9S1t3LhRf/zjH3XXXXedhCOJjzo6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Nq1evbpLn2Htg/UZe/bs8cat471jxw5vXLKHu0lcf9nZ2aEhbnr16uXd3hr6JxaLeePWEEKS9OUvf9kbX7hwoTduHdcBAwZ449aQQO73MRqNhtatIcKs70ufPn28ceu6tIYT+yA5oqmpyRu3ro9Ulsl5WArnYvJwWDrlYSmci8nDYemch7mDDAAAADjoIAMAAAAOOsgAAACAgw4yAAAA4KCDDAAAADhSehSL7OzsYNmqzLWqNQ8ePGi+f0lJiTduVUlb1ZpWJaXVJut9JCkSiUiScnNzVVpaGsStqsxVq1Z54/X19d64VYk6aNAgs02HDh3yxhsbG73xI0eOmO/lM3jw4GA5Ozs7OD7WPkh2haylurraG08c747cUSVcR48e9catCmnJroZOXGfxeDxUxW2NEGBV/w4cONAbt6qtJbtK+t577/XGv/71r3vjubm5XWrTyJEjg+X8/PzQumXKlCne+DvvvOONuyMQuKzj6l5/HR07dswbt6qqkx3zVJXJeVgK52LycFg65WEpnIvJw2HpnIe5gwwAAAA46CADAAAADjrIAAAAgIMOMgAAAOCggwwAAAA4UnIUi0Tlc1tbW7BsVdRaVZzJqmzz8/O98X79+nnje/fu9cat6lirSvrdd98125TQ2tqqAwcOBOvWfo8fP94btyqbs7L8fyslqzK3XmPNPR+Px71xq0I7Go2GXptYtypUJWnbtm3e+IgRI7xxq/rcqvKtra31xrOzs71x63hL0u7du73xyZMnS2o/vm7Fr1X9W1dX541bFbvW+0hSXl6eN25VST/xxBPe+C233OKNW/vsfh9jsVho5IGCggLva1auXOmNW9956/tVVFTkjSer9nevTVdZWZk3fvjwYfO9UlUm52EpnIvJw2HplIelcC4mD4elcx7mDjIAAADgoIMMAAAAOOggAwAAAA46yAAAAICDDjIAAADgSMlRLBJzz7e1tQXL06ZN8267ceNGb9ya412S9u/f741b1ah79uzxxocPH+6NW9WgpaWlZpsSc9XH4/FQO6xqzV27dnnjVqWopaSkxPw36zOs6marKt2d897VsZLXqlh1TZw40Ru3jrlVfd7Q0OCNW5W5LS0t3nj//v29cam9Ct4nUQ3d1tYWqoy22mpVhlvXcbKq4AEDBnjj1n5bVdK//OUvvfErr7zSG+94/NxKe6vC3arst0Y5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
"
class="
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>The diagonal values represents the variance of a random variable $C_x(k,k)$<br> <strong>Let us see the covariance of two correlated process in the cell below</strong></p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[266]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">m</span> <span class="o">=</span> <span class="mi">100</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">50</span>
<span class="n">xn</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="n">loc</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span><span class="n">scale</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">size</span><span class="o">=</span><span class="p">(</span><span class="n">N</span><span class="p">,</span><span class="n">m</span><span class="p">))</span>
<span class="n">b</span><span class="p">,</span> <span class="n">a</span> <span class="o">=</span> <span class="n">sig</span><span class="o">.</span><span class="n">butter</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span>
<span class="n">yn</span> <span class="o">=</span> <span class="n">sig</span><span class="o">.</span><span class="n">lfilter</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="n">a</span><span class="p">,</span><span class="n">xn</span><span class="p">,</span><span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
<span class="n">Cov</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">xn</span><span class="p">,</span><span class="n">yn</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[267]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov</span><span class="p">,</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">Cov</span><span class="o">.</span><span class="n">transpose</span><span class="p">(),</span><span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;k&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;l&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Transposed&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">25</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="s1">&#39;C(xn,xn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">25</span><span class="p">,</span><span class="mi">75</span><span class="p">,</span><span class="s1">&#39;C(xn,yn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">75</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="s1">&#39;C(yn,xn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">75</span><span class="p">,</span><span class="mi">75</span><span class="p">,</span><span class="s1">&#39;C(yn,yn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">25</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="s1">&#39;C(xn,xn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">25</span><span class="p">,</span><span class="mi">75</span><span class="p">,</span><span class="s1">&#39;C(yn,xn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">75</span><span class="p">,</span><span class="mi">25</span><span class="p">,</span><span class="s1">&#39;C(xn,yn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="mi">75</span><span class="p">,</span><span class="mi">75</span><span class="p">,</span><span class="s1">&#39;C(yn,yn)&#39;</span><span class="p">,</span><span class="n">fontsize</span><span class="o">=</span><span class="mi">14</span><span class="p">,</span><span class="n">color</span><span class="o">=</span><span class="s1">&#39;white&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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tG7dOh122GH617/+5X5GSWjNmjXOpuSyefNmZ1MG5l/SYWmYwlJMhSVRD9aJ44DXZ2dnKxKJeHJQsH5hqXXCoubDlqhIvtxGmY8J3SkzU+YbPHiws0eOHCmpahyfc845Ki0t1YQJEzRv3jxFo1Htt99+uvDCC3XiiSeqb9++6tixo9555x3l5OQoLy9P0WhUeXl51SR7/qINS0XFZw1LDM/+or8IizKntLdz506tX79eI0eO1DPPPBOaRozX01/sSiasrdSvX1/RaNQbP+aHa+aHGzZsqNatW+vee+9VSUmJ88WJREJDhw7V9ddfr3fffVcDBgxQly5dNGPGDDe29oYflqrmANs+6IclOV986qmnujRh5of3jh+WqubE/fffr9LSUt1xxx364osvFI1GNWLECOeLBw8e7HxxcsxEo9FqKfZ+Dn64fv36WrZsmfPFXC72U/jh9PDURo259NJLJUnnn3++3nrrLa1Zs0aFhYV6+umn9etf/1qSdPTRR+uDDz7w1hONGzdOU6ZMcf/Oy8vTa6+9phtuuEFSlUTz3nvvaciQIZoyZYreffdd/eMf//B2cArSsWNHvffeezr66KPdsYMPPliff/65Bg4cKEnaZ5999PDDD+u0007Ta6+9plmzZumaa66p5rRmzpypY4455r9sHWN3cPzxxysSiejcc8/VzJkztXr1aq1cuVLTpk1zadxGjBihjz76yP2iatu2rXr16qVevXp5ZZ1wwgmaPXu2MjMzNWTIEC1ZskT77befpk+frvfee09Tp05Vz549Q+vSvn17vfTSS94vjf3220/z5s1Tv379JFVJdvfdd5/OPPNMzZ49Wx9++KFuueUW7xeWJM2ZM0dHHnnk7mgiw3C++Le//e33+mK+0E2ePLlGvnjo0KHOF99zzz3f64tnzJjxvb74nnvucb745ZdfDvXFLMfYe1x++eXOF7/66qvOFz/77LOhvliq+kPywQcfdP+uV6+eXnzxRV177bWSpKFDhzpf/I9//MP54u7du4fW5ayzztLEiROrHZ88ebKuuuoqSf/xxb/+9a+dL/6///u/veaL7QW5DtGoUSMNHTpUzz33XMoAx+RfqoMHD9bixYu9n/3lL39Rr1699Lvf/U6SdMMNN6iiosL7ciJJF1xwge69916dccYZ2r59u4uUT0VhYaHuvPNOXX755crPz1eTJk10++2364EHHtDChQvdeUOHDlXXrl11/vnna+zYsTr44IN10kkneWV9+umn6tevXzVnbexZ6tWrp27duunZZ5+t9qVL+s9XiAEDBniBShs3blRJSYmOO+447/zRo0frxRdf9L4uXHbZZRo3bpxOO+00bd++XbfccktofdauXav7779fl1xyiRtj119/vSZMmKBPP/3UnTd48GB17dpVv/nNb3TZZZdp5MiROuOMM7yyFi9erN69e9sYM/5rGjZs6HxxqnmyK1981VVXeb74+uuvT+mLL7roIueLi4qKvtcX/+1vf3O+uFmzZil98aBBg5wv/tOf/hTqi/v06WPzZC9Tr1497bvvvt/ri/v16+f5YqkqMLB79+7uD7WrrrpKFRUVuuuuu7zzLrvsMvdH0/bt2/WnP/0ptD6vvPKKOnTooN69e7tjHTt21MCBA/Xcc8+5Y4MHD1a3bt2cLz788MP3mi+ulUssysvLVVhY6O0Xzz3iGQ3JaEZG0DIyVPKlug8//NDZlKl4Df+ioZwSluieEhIlvwMOOMDZwZdWShqlpaWqqKjQpk2bPBmD0a6U85599lln77///pKqlldEo1Ft27ZNLVu29Bwvk/fn5+crGo2qS5cuLqq1vLxc48eP1w033KD8/Hwdf/zxuv76690Xv6Qkd8cdd2ju3LmSpL/97W96/PHHtX37dm3atMl7nqTU+fzzz2v//ffXddddp23btmndunWaPHmy8vLylJeXp0gkotLSUl144YVOUjrqqKM0aNAgTZgwwclURUVFysrKUs+ePd2+9IwIpxwVlLaScLJRBgrbeYr9QMmPf4kHZRxeT0mIMmlxcbFisVi1fefDygmLzGU0PsvnPJDkzSPWndez/ZjInzLpwQcfrJYtWyoajapVq1buZffFF1905yTnQatWrbR9+3Y3X9q0aaPi4mIdffTReuKJJ1RRUaF99tlH/fv319///ne1bdvW1fvxxx/Xhg0bVFxcrClTpuihhx5SJBJx/c55lJWVpb///e/q27evbrjhBm3btk2FhYWaMGGCkxCj0ahKSkp02223qaKiQhs2bNAbb7yhYcOGua8o27Zt08qVK5WVlaXs7GyvndielEM53ukX2Ga1mcLCQpWXl3vPZn74+/2wJPXp08f5YrYT/XBWVpbzxVwuUFZW5vni4447Ttddd5169eqlBQsWOF88fvx4F1Ny++2368knn9T27du1fPlyVxaXnDz22GP6xS9+oeuuu07bt293vji54UgkElFRUZHzxWvXrtWbb76pQYMGeT416IvND+95Pyypmi9O5YelKt+b9MXJZVEZGRl68MEHdcUVVyg/P1+jRo3SxRdf7JbwJMfE448/rs8//1ySqvnioB9etWqV3n77bY0cOdK9I5x33nlavHixli1bpqysLM8Xx2IxbdiwQa+++qrzxcnlPklf3Lp1a7fJz0/hh+0Lch2iptt2ZmdnV9vlR6rabeatt97SWWedpUmTJnnroZLwL9HkJAw6giA33nijOnTooCFDhui6666rFiiwatUqzzF8/fXX1dY3JR2KfbWoHeTm5lYbYyUlJaqsrHQvEkcccYSWLl2q1atXe+fxF25yzer3jbGrr77ajbGrrrqq2hhbuXJltTEWLDM5xoJyn2H8UHanL37iiSe+1xcnX+Br6ouTL8rBebJ06VLzxWlG2Bj74IMPNHv2bJ188smaOnWq53eT/FBf/MQTT+iYY45RTk6OotGojj32WO/rcbLMmvrin3qM2QtyHaKwsFDxeLzaVqVBioqKvC8+SbKystSjRw/FYjHvr13CrzXJv8y/bzF8t27d1KBBA2VnZ6tVq1bVfs7Jkiw3WGYyX2Yw36WxZykqKlIikai2tWuQrVu3el/FksyZM0dHHHGEotGohg8frhkzZlQ7J9UY+74Xjh49ergxxpy3qcpMlhssM/nFYVdflAyjJmzcuHG3+WIGQ5KfwhcHg93MF/98qakvLioqSumLs7Ky1LVrV8VisWrBtEl+qC9+6623VFZWpiOPPFKHHHKIGjRooFdeeSW0zGS5Yb6Y25X/FNTKJRaVlZXasmWLCgoK3LGwZOEff/yxsxmNHPzLY8GCBc6mzMWo23322cfZdArsJMo9lAspow0YMMDZ/GXNCG7Jl/rat2+v7OxstW/f3pNf6Dz5i5ty3uOPP+7s9957TyNGjNC9997rRWt/8sknatiwob777jt98cUXatq0qdavX+/JYOedd54yMjJ0/vnn6/7779cbb7yhmTNnSpIOP/xwSVVyTTKRenIQd+vWTdFo1IsmTcoeDRo00B133KF///vfysnJ0V/+8hedfPLJKikpcX/VxuNx7y/IzMxMRSIR5ebmOomrT58++vrrr71Idk4qjhVKU0ygTyfAl3JKe/x6yL5mOewHSsOS/9c1+5cyULL9EomE17+8N+vHxPW8H/uOcyIYpc/r+UuN1zNhP2UqRvInI5J79+6tgQMHavbs2SovL3eSn1T15au4uFhLly5VXl6eFi1aJKmq7cvKyvTII4/oX//6lw4//HDl5ubq1VdfdTJrsr22bNmibdu2KTs727VDMpVcsJ0qKipUv3593XPPPZo+fbpycnJ0xx13uCwbUtUvgszMTDVo0MD1QyQSUSQScVHnubm56tevnzZv3qzy8nKv7zkf6dyDfZ+E4682s2XLFlVWVnrjwfxwzfzwWWed5XzxpEmTnI/55JNPJFWtUa5fv77zxazD1q1bNXbsWM8XP//885o5c6batWvnlrk0adLE+cDkUrhu3bp5kj39zsCBA50v3rlzp/PFvHd2drbzYUn/G4lEvOfv06ePNm/e7Hyx+eG944elqvGX9MX0w6+99przdx9//LHzxcm2Lysr0xlnnKGMjAxdddVVuu222/TWW2+5JTvJuZb0AWyLpC8O+uEkr776qk455RQVFxdrzpw5kv4zf5K+mPM6mVEjKyvLlZn0xaWlpe7YT+GH7QtyHSMZ0DR16lQNHz5c7du3V4cOHXTGGWe4v+Tef/999e/f37tu6NCh+tWvfqXrrrtO8+fP14MPPqibbrrpeyW77+Paa6/Vd999p8cff1xTpkxRSUmJrrnmmh9cTr9+/TRv3rz/qi7G7uG+++5TJBLR73//e/Xp00ctWrRQixYtNGzYMPeS8P7772vfffetdu2aNWv02Wef6bzzztOcOXO8X3g/lj/+8Y/avn27HnnkEZfy6MdspZzMDmAYu4OkL37kkUecL+7cufP3+uIDDjjA88X333//bvHF559/vvPFd99993/li22e/Dx44YUXUvriX/3qV84Xz5w5s5ovbtCggUaNGqXbbrtNixYt0mOPPaarr776e79G17ROAwcO1IEHHuiti/4h7ClfbC/IdYwNGzbo9NNP1wcffKALLrhAkydP1j333KMRI0bouuuuk1T112WHDh1c7szGjRtr7NixmjBhgj777DNJ0qRJk7RixQrdfPPNP+j+s2bNculljjnmGB166KEaN26cYrGYKisrdc0112jEiBE/KE1QVlaWDjrooB892Yzdy1dffaUHHnhAK1as0MiRI3XRRRdpzJgx6tmzp269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X+Ddd9/FBRdcgJycHCxYsACTJk3C7t27nWS3cOFCnHrqqZg+fTqSwXIP90dzZFnL49eSaCxP8uC/8ZwNBrLfU158P+fDf1GzNMf1Dkq0LHuyBM1e0ixNHXTQQS7N76B3/29+8xuEQiGMHTsWNTU1bl6vX78eb731FrKysnDSSSdhyZIliMViyMjIQOfOnXHIIYegb9+++Pjjj12eY8aMwcSJEzF69GgMGDAAU6dOxTXXXIOrrroKvXv3xpo1a3DHHXf4gu6z5HfVVVdhxIgROP/8833v2u9//3t88sknmDJlCm688UZ06NAB//znPzFu3Djk5OTgjTfewH333efySiQS+L//+z+cfPLJeOaZZ0zJkPvZ8q4PbiFJVbwDFKw5LTts2+FIJOJs8Y033uje1fLycnz++eeYP38+otGos8U5OTnIyclBp06d8OSTT+Kyyy7DRx99BKChn8aMGYOrr74aZ555JgYOHIjp06djwoQJmDBhAvr06YNPP/0Uv/zlL/Hhhx82ssMA0L17dzzyyCO4//778corr2Djxo049thjMXXqVFx77bX48MMPUVxcjF/96lfOFmdnZ+O1117DpEmTfG1buHAhRo8ejccff7xRObLD+84OA8BPfvITZ4s5gsuWLVucLR45cqSzxQCcLR4wYIDPro4ePRpXXXUVRo8ejX79+mH69Om45pprcOWVV7rf97fffrubl2yHMzIycNlll2HEiBG4+OKLfdenTJmCTz75BHfddRduueUWdOjQAYsWLcJ//Md/ICcnB2+++Sbuvfde1NbWuv72bDHPsW/DDstJrxXRrl07DB48GC+++GLSECfeS3344Yf7wh4BwO23344DDjgAF154IQDghhtuQDQaxf333++7b/z48Zg6dSrGjRuHyspK3HXXXWZ9XnrpJfTo0cP3ovfq1QuHHXYYnn32WXdt4MCBKC0txY033ojbbrsNJ510EsaOHevL68MPP8QhhxzSyOiIfUv79u0xbNgwPPnkk41CeAH//ijp27cvPvnkE3d906ZN2LVrF0aPHu27/+yzz8a8efN8vwTHjx+P6dOnuzn261//2qzPCy+8gJ49e6Jfv37uWvfu3dG/f3/MnTvXXTv00EPRu3dvXH311fj5z3+OE088Eeedd54vrw8//BB9+/ZttJ9RiK9K27Ztv5Yt3rx5MxYvXowzzzzTd/9ZZ52FuXPn+t6Tq6++2tniioqKJm3x+vXr8cADD2DixIno3LkzCgoKcPvtt+PBBx90CxyA3xb/9Kc/NW3xoEGDZItbmPbt2+Poo4/eoy0eOHBgUlt89tln++4/88wzk9pi/n3/v//7v2Z9PFt8yCGHuGvNscXHH3+8aYu/7TmmD+RWRJcuXRAOh7F+/fom7+vcuTO2b9/uu7Zjxw7ceeeduOKKK3DFFVdg5MiR+MUvfuH7KxEAHnroISxZsgTr1q3DH/7wB/Tu3bvRsawe27Ztwz//+U+cdtpp7tr3vvc9LF++3LeKWF1djXvvvRfr1q3Du+++i/nz5+Ooo45qVL9kR8CKfUv37t0RDoexdu3aJu8rLi72rRQBDatnp512mvsA7dWrFwYOHIgXX3zRd99DDz2EpUuXujlWUlLiOzKX2bp1K95++22fsT/jjDPw8ccfY/Xq1e7arl27cNddd+Gzzz7DokWL8Oqrr+KII47w5bV9+3ZkZmaazi5CNJdvYotfeOEFjBgxotF7EvTBeOCBB5wtnj59epO2GADmzp2LZcuW4Wc/+xluv/12rF+/Hg8++KDvHrbF77zzjmmLs7KyZItbmOba4v333z+pLT711FN9c6x///5JbTH/vm+OLT799NPdtVGjRiW1xZMmTXK2+LXXXmsxW5ySWyzC4TByc3PNc7X5rwqWFTZs2ODSPXr08OXJeXGan2fZhCU5dkZgKXHbtn7TrR0AACAASURBVG0uzcHxWfJjL9Ogd2f37t1devPmzYhGo9i8ebPvry0OYs/BxTkIvjf5vI/Z+vp61NbW+j5ug8G7o9EoMjIyfJLECy+8gCFDhuCSSy7B3XffjVWrVrl/8ySetWvXuvZ5xt/7GGJp1Xvxnn/+edxyyy2YMmUKotEozjrrLEyfPh3RaBQVFRWIx+P49NNPfR6+27ZtQ//+/QH821vYk6Q6derk/jK25gePaVAG8mCPZJZiWFILejx78PwLHnrBf8lbch7THKcJy3M7WLZHcJ7x3OR2cPB59pLmeziIfSgUQq9evQA0BH335iC/B977kZmZidraWlffrKwsVFVVoU2bNjj55JPx97//HWPGjPH9seSN54oVK7B7925EIhGXd2FhoasvtzsUCuHZZ5/Fr371K0ydOtXJ1jNnznRzPhaLYfXq1aiurnbzZMOGDejbt697t736ee23vKybg+XFnWrk5uYiHA775oPs8J7tMLetvr7e1x62w579jUajPjv84osv4oYbbsCRRx6Jl156CRMmTMDy5cuxevVq39bD999/37XRO1CluLjY98HEczcajeLuu+/GY489hh49euDss89GXV2di+rRlC1muxa0xbLD+94OA2hki5PZYaBhDni22JsPe7LF3u/yFStWuP4L2uKgHQbgbPHvfvc7RKNRjBgxwtni2tpaZ4t5i8nGjRtx8MEHY+fOnb76Af+OdOW146vQHDusFeRWxPr16xGPxxv9UgpSUVHhe1k9srKyMGDAAESjUTOPZCcLNbXX5+2338bu3btx/PHHY8iQIWjXrh3mzJlj5unlGwyR4+1lDJ5OJPYtW7duRTweR8+ePZu8r7KyMukcmzt3Ls466yxEIhGMGjWq0YoF8NXn2Jtvvondu3fjxBNPxLBhw9C2bVu88sorZp5evppj4ttiw4YNX9sWR6NRPP/88zj33HMRiURw+umnJ43g81XfEwAoKSlBmzZtzBVgvSepw962xXtjjr355puora1NGVusD+RWxM6dO7F48WKMGTPGtyLh4TkJfPTRRygtLW307zfddBOysrLwn//5nzjnnHNw/PHHf+M6xWIxzJs3D6NGjcKoUaMwf/78rxUeqE+fPti6davv6Fmx76mursbKlStxzjnn+Fb3PLw59umnnyY13LNnz8bgwYNx7rnnIi8vb69EUonFYnjhhRdw5pln4owzzsAbb7zxtcID9e7dW3NM7BW+qS1++umncdRRR+GCCy5AXl7eXoly0aZNG9x8883461//iieeeAJ33XWXb6WxucgWfzeorq7G4sWL92iLV61a1SxbvDfmWCwWw9y5c50t/sc//vGdtsUpqfXFYjFUVVX5/uph+Z5lGZY6WEoJblrnv3pYsmF5iJf92aixZMge0Js3b3ZpSzZimSnorMGevW3atEFGRgaKi4t9Uh3XdcSIES593HHHuTTvYZs2bRomT56MBx98EPfffz9WrVqFUCiEM844A+PGjcP3v/99/Otf/8KoUaN8XuFHHHEEzj//fFxyySVYvnw5HnzwQdxyyy245JJLUFZW5vq/trbW9aX3/3bt2iE/P983mXlcZs2ahWeeeQaJRAJXXHGFk0q8exKJhC94f2ZmJsLhMPLy8tx2ikGDBuGtt97yecWzJ7t1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
"
class="
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Finally, It will  also be useful to display the filtered random process.</p>

</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[269]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">5</span><span class="p">),</span><span class="n">sharex</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">xn</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">stem</span><span class="p">(</span><span class="n">yn</span><span class="p">[:,</span><span class="mi">1</span><span class="p">],</span><span class="n">use_line_collection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$n$&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$xn$&#39;</span><span class="p">)</span>
<span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">r</span><span class="s1">&#39;$yn$&#39;</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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2PrZz36mvr4+9fX16corr9S3vvUt6scCTz31lNatW6d//ud/ViaTkRTcfYcuyxz27dun8847T9OmTVNpaamuuOIKbd++3XSxYm327NnDfoVs375dV111lSTpqquuoo4MmTx58uAg1/Hjx2v69Onq6uqifiyQSCR01llnSZL6+/vV39+vRCKhXbt2qba2VpJUV1dH3RjU2dmpHTt2aPHixZKkbDZL/VgsqHaN/GcOXV1dmjJlyuDrKVOmaO/evQZLhJH87W9/0+TJkyUNBAVHjhwxXCK0tbWptbVV73rXu6gfSziOo9WrV+uvf/2rrr76ak2bNk0TJkxQSUmJJKm8vFxdXV2GSxlfjz32mG6++WYdO3ZMktTT00P9WGT9+vWSpA996EPKZDKBtWsEZDmMNPk0kUgYKAkQHsePH9emTZt06623asKECaaLg1OSyaTuv/9+vfnmm9q4caMOHDhgukg45cUXX9SkSZM0c+ZM7dq1y3RxcIZ169apvLxcf/vb3/SVr3xFlZWVgR2LgCyHKVOmqLOzc/B1Z2fnYEQMe0yaNEmHDx/W5MmTdfjwYcb4GdTX16dNmzZp4cKFet/73ieJ+rHN2WefrdmzZ2vv3r36+9//rv7+fpWUlKirq0vl5eWmixdLe/bs0e9+9zv9/ve/18mTJ3Xs2DE99thj1I8lTn/vkyZN0vz587Vv377A2jXGkOUwa9YsvfHGG2pra1NfX5+ee+45zZs3z3SxcIZ58+bpmWeekSQ988wzmj9/vuESxVM2m9XDDz+s6dOn69prrx3cTv2Yd+TIEb355puSBmZcvvzyy5o+fbouvfRStbS0SJKam5tp3wz56Ec/qocffliNjY264447dNlll+n222+nfixw/PjxwW7k48eP66WXXtKMGTMCa9dYGHYUO3bs0OOPPy7HcbRo0SJdd911posUaw8++KB2796tnp4eTZo0ScuXL9f8+fP1wAMPqKOjQ+l0Wp/73OdYVsGAP/7xj/rSl76kGTNmDHbt33jjjbrwwgupH8Nef/11NTY2ynEcZbNZvf/979f111+vQ4cODVtWIZVKmS5urO3atUs/+clPtGbNGurHAocOHdLGjRslDUyIufLKK3Xdddepp6cnkHaNgAwAAMAwuiwBAAAMIyADAAAwjIAMAADAMAIyAAAAwwjIAAAADCMgAwAAMIyADAAAwDACMgAAAMN4liUAnPL000/rxRdfVEVFhZ5//nmVlpZq1apVmjNnjumiAYg4MmQAcMr+/fv16quvat68eXrkkUeUyWS0bds208UCEAMEZABwyuuvv66lS5fqve99r5LJpKqqqkwXCUBMEJABwCn79+/X3LlzB1//+c9/1vTp0w2WCEBcEJABgKS2tjY5jqPKysrBba2traqpqTFXKACxQUAGABrorpwxY4aSybeaxT/96U8EZACKgoAMADQQkJ1//vmDr3t6etTd3a3q6mqDpQIQF4lsNps1XQgAAIA4I0MGAABgGAEZAACAYQRkAAAAhhGQAQAAGEZABgAAYBgBGQAAgGEEZAAAAIYRkAEAABhGQAYAAGDY/weYtX/d5APLpQAAAABJRU5ErkJggg==
"
class="
"
>
</div>

</div>

</div>

</div>

</div>
</body>







</html>
