# MOVIE RECOMMENDER SYSTEM

Una reconocida plataforma de Streaming, nos proporciona de toda su data sobre las películas en su sistema, con la finalidad de poder crearle un recomendador de películas virtual. De esta manera el público objetivo podrá interactuar con la platadorma de forma más amigable.

![image](https://github.com/user-attachments/assets/ad2c1308-59bc-487f-9438-11303ad0db75)

Como científicos de datos, hemos diseñado varios métodos de recomendación de películas, con la finalidad de poder determinar cual es el que nos brinda el mejor desempeño y calidad al momento de que el usuario interactúa en la plataforma. Entre los métodos utilizados están los siguientes:

  1. Recomendador no personalizado

  2. Recomendador Content-based

  3. Recomendador Collaborative filtering

## ARQUITECTURA DEL PROYECTO

<mxGraphModel><root><mxCell id="0"/><mxCell id="1" parent="0"/><mxCell id="2" value="" style="group" vertex="1" connectable="0" parent="1"><mxGeometry x="88.17" y="40" width="950.83" height="444.5" as="geometry"/></mxCell><mxCell id="3" value="&lt;b&gt;Matrix&lt;/b&gt;&lt;div&gt;&lt;b&gt;Coseno&lt;/b&gt;&lt;/div&gt;&lt;div&gt;&lt;b&gt;Similitud&lt;/b&gt;&lt;/div&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#F54749;gradientDirection=north;fillColor=#C7131F;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.cloud_directory;labelBackgroundColor=#ffffff;" vertex="1" parent="2"><mxGeometry x="551.83" y="318" width="78" height="78" as="geometry"/></mxCell><mxCell id="4" value="&lt;b&gt;Modelo&lt;/b&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.glue;labelBackgroundColor=#ffffff;" vertex="1" parent="2"><mxGeometry x="561.8300000000003" y="72" width="78" height="78" as="geometry"/></mxCell><mxCell id="5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="2" source="7" target="26"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="2" source="7" target="26"><mxGeometry relative="1" as="geometry"/></mxCell><mxCell id="7" value="&lt;b&gt;Dataframe&amp;nbsp;&lt;/b&gt;&lt;div&gt;&lt;b&gt;Final&lt;/b&gt;&lt;/div&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;labelBackgroundColor=#ffffff;spacingTop=5;" vertex="1" parent="2"><mxGeometry x="381.8300000000002" y="170" width="78" height="78" as="geometry"/></mxCell><mxCell id="8" value="&lt;b&gt;Análisis de datos&lt;/b&gt;&lt;div&gt;&lt;b&gt;EDA&lt;/b&gt;&lt;/div&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.elasticsearch_service;labelBackgroundColor=#ffffff;" vertex="1" parent="2"><mxGeometry x="201.8300000000002" y="103.5" width="78" height="78" as="geometry"/></mxCell><mxCell id="9" value="" style="verticalLabelPosition=bottom;aspect=fixed;html=1;shape=mxgraph.salesforce.data;" vertex="1" parent="2"><mxGeometry x="1.8299999999999983" y="43.5" width="78.17" height="96.5" as="geometry"/></mxCell><mxCell id="10" value="" style="verticalLabelPosition=bottom;aspect=fixed;html=1;shape=mxgraph.salesforce.data;" vertex="1" parent="2"><mxGeometry x="1.8299999999999983" y="318" width="78.17" height="96.5" as="geometry"/></mxCell><mxCell id="11" value="" style="verticalLabelPosition=bottom;aspect=fixed;html=1;shape=mxgraph.salesforce.data;" vertex="1" parent="2"><mxGeometry x="1.8299999999999983" y="181.5" width="78.17" height="96.5" as="geometry"/></mxCell><mxCell id="12" value="&lt;div style=&quot;&quot;&gt;&lt;font size=&quot;1&quot; color=&quot;#232f3e&quot;&gt;&lt;span style=&quot;text-wrap: nowrap; background-color: rgb(255, 255, 255);&quot;&gt;&lt;b style=&quot;font-size: 12px;&quot;&gt;Movies&lt;/b&gt;&lt;/span&gt;&lt;/font&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="2"><mxGeometry x="0.9099999999999966" y="140" width="80" height="30" as="geometry"/></mxCell><mxCell id="13" value="&lt;div style=&quot;&quot;&gt;&lt;font size=&quot;1&quot; color=&quot;#232f3e&quot;&gt;&lt;span style=&quot;text-wrap: nowrap; background-color: rgb(255, 255, 255);&quot;&gt;&lt;b style=&quot;font-size: 12px;&quot;&gt;Links&lt;/b&gt;&lt;/span&gt;&lt;/font&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="2"><mxGeometry y="414.5" width="80" height="30" as="geometry"/></mxCell><mxCell id="14" value="&lt;div style=&quot;&quot;&gt;&lt;font size=&quot;1&quot; color=&quot;#232f3e&quot;&gt;&lt;span style=&quot;text-wrap: nowrap; background-color: rgb(255, 255, 255);&quot;&gt;&lt;b style=&quot;font-size: 12px;&quot;&gt;Ratings&lt;/b&gt;&lt;/span&gt;&lt;/font&gt;&lt;/div&gt;" style="text;whiteSpace=wrap;html=1;align=center;" vertex="1" parent="2"><mxGeometry x="1.8299999999999983" y="278" width="80" height="30" as="geometry"/></mxCell><mxCell id="15" value="&lt;b&gt;Preprocesamiento&amp;nbsp;&lt;/b&gt;&lt;div&gt;&lt;b&gt;de datos&lt;/b&gt;&lt;/div&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#945DF2;gradientDirection=north;fillColor=#5A30B5;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.api_gateway;labelBackgroundColor=#ffffff;" vertex="1" parent="2"><mxGeometry x="201.82999999999998" y="270" width="78" height="78" as="geometry"/></mxCell><mxCell id="16" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="141.82999999999998" y="100" as="sourcePoint"/><mxPoint x="82.83" y="100" as="targetPoint"/></mxGeometry></mxCell><mxCell id="17" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="141.82999999999998" y="236" as="sourcePoint"/><mxPoint x="86.99999999999999" y="236" as="targetPoint"/></mxGeometry></mxCell><mxCell id="18" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="145.82999999999998" y="373" as="sourcePoint"/><mxPoint x="82.00000000000001" y="373" as="targetPoint"/></mxGeometry></mxCell><mxCell id="19" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="147.82999999999998" y="369.75" as="sourcePoint"/><mxPoint x="147.82999999999998" y="99.75" as="targetPoint"/></mxGeometry></mxCell><mxCell id="20" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="151.82999999999998" y="234.5" as="sourcePoint"/><mxPoint x="191.82999999999998" y="170" as="targetPoint"/></mxGeometry></mxCell><mxCell id="21" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="149.82999999999998" y="238.5" as="sourcePoint"/><mxPoint x="189.82999999999998" y="300" as="targetPoint"/></mxGeometry></mxCell><mxCell id="22" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="337.83" y="146" as="sourcePoint"/><mxPoint x="278.83" y="146" as="targetPoint"/></mxGeometry></mxCell><mxCell id="23" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="337.83" y="313" as="sourcePoint"/><mxPoint x="282.99999999999994" y="313" as="targetPoint"/></mxGeometry></mxCell><mxCell id="24" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="341.83" y="310" as="sourcePoint"/><mxPoint x="341.83" y="150" as="targetPoint"/></mxGeometry></mxCell><mxCell id="25" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="345.83" y="228.5" as="sourcePoint"/><mxPoint x="375.83" y="228" as="targetPoint"/></mxGeometry></mxCell><mxCell id="26" value="&lt;b&gt;Dataframe&lt;/b&gt;&lt;div&gt;&lt;b&gt;Vectorizer&lt;/b&gt;&lt;/div&gt;" style="outlineConnect=0;fontColor=#232F3E;gradientColor=#4D72F3;gradientDirection=north;fillColor=#3334B9;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;labelBackgroundColor=#ffffff;spacingTop=5;" vertex="1" parent="2"><mxGeometry x="381.8300000000002" y="328" width="78" height="78" as="geometry"/></mxCell><mxCell id="27" value="" style="endArrow=classic;startArrow=classic;html=1;rounded=0;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="240.46999999999997" y="262" as="sourcePoint"/><mxPoint x="240.32999999999998" y="222" as="targetPoint"/></mxGeometry></mxCell><mxCell id="28" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="2" source="26" target="3"><mxGeometry relative="1" as="geometry"><mxPoint x="491.83" y="380" as="sourcePoint"/><mxPoint x="511.83" y="293" as="targetPoint"/><Array as="points"><mxPoint x="471.83" y="380"/><mxPoint x="471.83" y="357"/></Array></mxGeometry></mxCell><mxCell id="29" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="551.83" y="130" as="sourcePoint"/><mxPoint x="459.83" y="208.5" as="targetPoint"/></mxGeometry></mxCell><mxCell id="30" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="561.83" y="160" as="sourcePoint"/><mxPoint x="459.83" y="327.25" as="targetPoint"/></mxGeometry></mxCell><mxCell id="31" value="" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=2;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="590.83" y="178" as="sourcePoint"/><mxPoint x="590.33" y="318" as="targetPoint"/><Array as="points"><mxPoint x="590.33" y="250"/></Array></mxGeometry></mxCell><mxCell id="32" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=3;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="641.83" y="100" as="sourcePoint"/><mxPoint x="721.83" y="30" as="targetPoint"/><Array as="points"><mxPoint x="661.83" y="30"/></Array></mxGeometry></mxCell><mxCell id="33" value="" style="endArrow=classic;html=1;rounded=0;strokeWidth=3;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="641.83" y="130" as="sourcePoint"/><mxPoint x="721.83" y="190" as="targetPoint"/><Array as="points"><mxPoint x="659.33" y="189.13"/></Array></mxGeometry></mxCell><mxCell id="34" value="" style="whiteSpace=wrap;html=1;aspect=fixed;fillColor=none;strokeWidth=3;" vertex="1" parent="2"><mxGeometry x="731.83" width="210" height="210" as="geometry"/></mxCell><mxCell id="35" value="" style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=default;verticalAlign=top;aspect=fixed;imageAspect=0;image=https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.svg;" vertex="1" parent="2"><mxGeometry x="721.83" y="150" width="229" height="63.55" as="geometry"/></mxCell><mxCell id="36" value="" style="endArrow=classic;startArrow=classic;html=1;rounded=0;strokeWidth=3;" edge="1" parent="2"><mxGeometry width="50" height="50" relative="1" as="geometry"><mxPoint x="836.71" y="55" as="sourcePoint"/><mxPoint x="836.3305653576172" y="155" as="targetPoint"/></mxGeometry></mxCell><mxCell id="37" value="Cloud Deploy" style="sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;fontColor=#999999;shape=image;aspect=fixed;imageAspect=0;image=data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGlkPSJzdmc2ODU4MSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMjM2LjQzMzk0IDI1My4zMDQ0MSIgaGVpZ2h0PSIyNTMuMzA0NDFtbSIgd2lkdGg9IjIzNi40MzM5NG1tIj4mI3hhOyAgJiN4YTsgIDxkZWZzIGlkPSJkZWZzNjg1NzgiLz4mI3hhOyAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTcuNjIzNTQxLC0xNy45ODI1NTIpIiBpZD0ibGF5ZXIxIj4mI3hhOyAgICA8cGF0aCBpZD0icGF0aDY4NzE1IiBkPSJtIC0xNy42MjM1NDEsMTI5LjE0Mjk5IDg0LjUwNjMyMiw0Ni44MDM1MSB2IDk1LjM0MDQ3IGwgLTQwLjE1ODU2LC0yMC41MTI2NSB2IC01Mi41ODE3MSBsIC00NC4zNDc3NjIsLTIyLjI0NjEyIHoiIHN0eWxlPSJvcGFjaXR5OjE7ZmlsbDojYjVjYmY5O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO3N0cm9rZS13aWR0aDowLjI2NDU4M3B4O3N0cm9rZS1saW5lY2FwOmJ1dHQ7c3Ryb2tlLWxpbmVqb2luOm1pdGVyO3N0cm9rZS1vcGFjaXR5OjEiLz4mI3hhOyAgICA8cGF0aCBpZD0icGF0aDY4NzE3IiBkPSJNIDM0LjAyMTMzOSw3NC4yOTk1NjkgMTM4LjM4ODEzLDEzNC44MDE1MyBWIDI1Ni4xNDM5NCBMIDkwLjUyODEyNiwyMzAuMDcxOSBWIDE2My4wNDQ2NiBMIDM0LjAyMTMzOSwxMzAuNTg3NTUgWiIgc3R5bGU9Im9wYWNpdHk6MTtmaWxsOiM3NjllZjU7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOm5vbmU7c3Ryb2tlLXdpZHRoOjAuMjY0NTgzcHg7c3Ryb2tlLWxpbmVjYXA6YnV0dDtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLW9wYWNpdHk6MSIvPiYjeGE7ICAgIDxwYXRoIGlkPSJwYXRoNjg3MTkiIGQ9Ik0gOTIuODg4OTc4LDgxLjQwMjY2IFYgMTcuOTgyNTUyIEwgMjE4LjgxMDQsOTIuNTkxNTY0IFYgMjM1LjI4NDMyIGwgLTU3Ljk5MjQxLC0zNC43ODA0MyB2IC03Ny40OTgxMiB6IiBzdHlsZT0ib3BhY2l0eToxO2ZpbGw6IzU5ODZmMjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZTtzdHJva2Utd2lkdGg6MC4yNjQ1ODNweDtzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utb3BhY2l0eToxIi8+JiN4YTsgIDwvZz4mI3hhOzwvc3ZnPg==;" vertex="1" parent="2"><mxGeometry x="861.83" y="70.75" width="49" height="52.77" as="geometry"/></mxCell><mxCell id="38" value="Cloud Deploy" style="sketch=0;html=1;verticalAlign=top;labelPosition=center;verticalLabelPosition=bottom;align=center;spacingTop=-6;fontSize=11;fontStyle=1;fontColor=#999999;shape=image;aspect=fixed;imageAspect=0;image=data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGlkPSJzdmc2ODU4MSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMjM2LjQzMzk0IDI1My4zMDQ0MSIgaGVpZ2h0PSIyNTMuMzA0NDFtbSIgd2lkdGg9IjIzNi40MzM5NG1tIj4mI3hhOyAgJiN4YTsgIDxkZWZzIGlkPSJkZWZzNjg1NzgiLz4mI3hhOyAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTcuNjIzNTQxLC0xNy45ODI1NTIpIiBpZD0ibGF5ZXIxIj4mI3hhOyAgICA8cGF0aCBpZD0icGF0aDY4NzE1IiBkPSJtIC0xNy42MjM1NDEsMTI5LjE0Mjk5IDg0LjUwNjMyMiw0Ni44MDM1MSB2IDk1LjM0MDQ3IGwgLTQwLjE1ODU2LC0yMC41MTI2NSB2IC01Mi41ODE3MSBsIC00NC4zNDc3NjIsLTIyLjI0NjEyIHoiIHN0eWxlPSJvcGFjaXR5OjE7ZmlsbDojYjVjYmY5O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO3N0cm9rZS13aWR0aDowLjI2NDU4M3B4O3N0cm9rZS1saW5lY2FwOmJ1dHQ7c3Ryb2tlLWxpbmVqb2luOm1pdGVyO3N0cm9rZS1vcGFjaXR5OjEiLz4mI3hhOyAgICA8cGF0aCBpZD0icGF0aDY4NzE3IiBkPSJNIDM0LjAyMTMzOSw3NC4yOTk1NjkgMTM4LjM4ODEzLDEzNC44MDE1MyBWIDI1Ni4xNDM5NCBMIDkwLjUyODEyNiwyMzAuMDcxOSBWIDE2My4wNDQ2NiBMIDM0LjAyMTMzOSwxMzAuNTg3NTUgWiIgc3R5bGU9Im9wYWNpdHk6MTtmaWxsOiM3NjllZjU7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOm5vbmU7c3Ryb2tlLXdpZHRoOjAuMjY0NTgzcHg7c3Ryb2tlLWxpbmVjYXA6YnV0dDtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLW9wYWNpdHk6MSIvPiYjeGE7ICAgIDxwYXRoIGlkPSJwYXRoNjg3MTkiIGQ9Ik0gOTIuODg4OTc4LDgxLjQwMjY2IFYgMTcuOTgyNTUyIEwgMjE4LjgxMDQsOTIuNTkxNTY0IFYgMjM1LjI4NDMyIGwgLTU3Ljk5MjQxLC0zNC43ODA0MyB2IC03Ny40OTgxMiB6IiBzdHlsZT0ib3BhY2l0eToxO2ZpbGw6IzU5ODZmMjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZTtzdHJva2Utd2lkdGg6MC4yNjQ1ODNweDtzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utb3BhY2l0eToxIi8+JiN4YTsgIDwvZz4mI3hhOzwvc3ZnPg==;" vertex="1" parent="2"><mxGeometry x="761.83" y="71.37" width="49" height="52.77" as="geometry"/></mxCell></root></mxGraphModel>

