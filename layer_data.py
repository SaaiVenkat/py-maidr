import numpy as np

class LayerData:

    def __init__(self, data):
        self.plot_data = data

    def dataplotCount(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []

        x_vars = self.plot_data.get_xticklabels()
        for x in x_vars:
            data_x.append(x.get_text())

        y_vars = self.plot_data.patches
        for y in y_vars:
            data_y.append(y.get_height())

        _data = [data_x, data_y]
        self.createHtmlTemplate(name, _data, 'path', 2)

        return _data

    def dataplotBar(self, name):
        _data = self.dataplotCount(name)
        self.createHtmlTemplate(name, _data, 'path', 2)

        return _data

    def dataplotScatter(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []
        data_sc = self.plot_data.collections[0].get_offsets()
        for points in data_sc:
            data_y.append(points.data[1])
            data_x.append(points.data[0])

        _data = [data_x, data_y]
        self.createHtmlTemplate(name, _data, 'use', 0)

        return _data

    def dataplotLine(self, name):
        if not self.plot_data.has_data():
            return "Plot is Empty!"

        data_y = []
        data_x = []
        # lineplot_data = self.plot_data.get_lines()[0].get_data()
        # x_data = lineplot_data[0]
        # y_data = lineplot_data[1]
        for data in self.plot_data.lines:
            y = data.get_ydata()
            data_y.append(y)

            x = data.get_xdata()
            data_x.append(x)    

        # values = {}


        # _data = [x_data, y_data]
        # print(":::: ",_data)
        # x_ = []
        # for x in data_x:
        #     x_.append(x)
        # y_ = []
        # for y in data_y:
        #     y_.append(y)
        # list(data_x)
        x = np.array(data_x[0]).tolist()
        y = np.array(data_y[0]).tolist()
        _data = [x, y]
        print("hjvhfhfhfhfhtftfhtftr45678987654ew345678987654", _data)
        self.createHtmlTemplate(name, _data, 'path', 14)

        return _data

    def createHtmlTemplate(self, name, _data, element, slice_count):
        # if name == 'line':
        #     for
        with open("generated_svg/"+name+"plot.svg", "r") as text_file:
            svg_ = text_file.read()

        id_attr = 'id="MyChart"'
        svg_ = svg_.replace('<svg ', f'<svg {id_attr}')

        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>

            <script src="https://cdn.jsdelivr.net/npm/chart2music"></script>
        </head>
        <body>
            <div>
                {svg}
            </div>
            <div id="cc"></div>

            <script>
                const x = {data_x};
                const err = c2mChart({{
                    type: "{name}",
                    element: document.getElementById("MyChart"),
                    cc: document.getElementById("cc"),
                    axes: {{
                        x: {{
                            label: "class",
                            format: (index) => x[index]
                        }},
                        y: {{
                            label: "count",
                            minimum: 0
                        }}
                    }},
                    data: {data_y},
                    options: {{
                        onFocusCallback: ({{index}}) => {{
                            Array.from(document.querySelectorAll("#MyChart {element}")).slice({slice_count})                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  .forEach((elem) => {{
                                elem.style.fill = "#595959";
                            }})
                            document.querySelectorAll("#MyChart {element}")[index+{slice_count}].style.fill = "cyan";
                        }}
                    }}
                }});
                if(err){{
                    console.error(err);
                }}
            </script>
        </body>
        </html>
        """

        html_template = html_template.format(
            svg=svg_, data_x=_data[0], name=name, data_y=_data[1], element=element, slice_count = slice_count)

        with open('chart.html', 'w') as f:
            f.write(html_template)

    
    # def createHtmlTemplateLine(self, name, _data, element, slice_count):
    #     with open("generated_svg/"+name+"plot.svg", "r") as text_file:
    #         svg_ = text_file.read()

    #     id_attr = 'id="MyChart"'
    #     svg_ = svg_.replace('<svg ', f'<svg {id_attr}')

    #     values = []
    #     for i in range(len(_data[0])):
    #         values.append({'x':_data[0][i], 'y':_data[1][i]})

    #     html_template = """
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Document</title>

    #         <script src="https://cdn.jsdelivr.net/npm/chart2music"></script>
    #     </head>
    #     <body>
    #         <div>
    #             {svg}
    #         </div>
    #         <div id="cc"></div>

    #         <script>
    #             values = {data}
                
    #             const datasets = [{{
    #                 label: "O'Hare",
    #                 backgroundColor: "navy",
    #                 borderColor: "navy",
    #                 data: data.map(row => row.y),
    #                 hoverRadius: 10
    #             }}];

    #             const config = {{
    #                 type: "line",
    #                 data: {{
    #                     labels: data.map(row => row.x),
    #                     datasets
    #                 }},
    #                 options: {{
    #                     plugins: {{
    #                     legend: {{
    #                         display: true
    #                     }}
    #                 }}
    #                 }}
    #             }};

    #             const myChart = new Chart(canvas, config);

                
    #             const err = c2mChart({{
    #                 type: "{name}",
    #                 element: document.getElementById("MyChart"),
    #                 cc: document.getElementById("cc"),
    #                 axes: {{
    #                     x: {{
    #                         label: "class",
    #                         format: (index) => x[index]
    #                     }},
    #                     y: {{
    #                         label: "count",
    #                         minimum: 0
    #                     }}
    #                 }},
    #                 data: {{'vvv': data.map(row => ({{ x: row.x, y: row.y }}))}},
                    
    #             }});
    #             if(err){{
    #                 console.error(err);
    #             }}
    #         </script>
    #     </body>
    #     </html>
    #     """

    #     html_template = html_template.format(
    #         svg=svg_, name=name, data=values, element=element, slice_count = slice_count)

    #     with open('chart.html', 'w') as f:
    #         f.write(html_template)
