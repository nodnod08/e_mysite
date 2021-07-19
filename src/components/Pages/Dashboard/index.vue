<template>
  <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4 pt-5">
    <div id="container"></div>
    <br />
    <br />
    <div id="container-1"></div>
  </main>
</template>

<script>
export default {
  mounted() {
    const chart = Highcharts.chart("container", {
      chart: {
        type: "bar",
      },
      title: {
        text: "Fruit Consumption",
      },
      xAxis: {
        categories: ["Apples", "Bananas", "Oranges"],
      },
      yAxis: {
        title: {
          text: "Fruit eaten",
        },
      },
      series: [
        {
          name: "Jane",
          data: [1, 0, 4],
        },
        {
          name: "John",
          data: [5, 7, 3],
        },
      ],
    });

    const chart1 = Highcharts.chart("container-1", {
      chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: "pie",
      },
      title: {
        text: "Browser market shares in January, 2018",
      },
      tooltip: {
        pointFormat: "{series.name}: <b>{point.percentage:.1f}%</b>",
      },
      accessibility: {
        point: {
          valueSuffix: "%",
        },
      },
      plotOptions: {
        pie: {
          allowPointSelect: true,
          cursor: "pointer",
          dataLabels: {
            enabled: true,
            format: "<b>{point.name}</b>: {point.percentage:.1f} %",
          },
        },
      },
      series: [
        {
          name: "Brands",
          colorByPoint: true,
          data: [
            {
              name: "Chrome",
              y: 61.41,
              sliced: true,
              selected: true,
            },
            {
              name: "Internet Explorer",
              y: 11.84,
            },
            {
              name: "Firefox",
              y: 10.85,
            },
            {
              name: "Edge",
              y: 4.67,
            },
            {
              name: "Safari",
              y: 4.18,
            },
            {
              name: "Sogou Explorer",
              y: 1.64,
            },
            {
              name: "Opera",
              y: 1.6,
            },
            {
              name: "QQ",
              y: 1.2,
            },
            {
              name: "Other",
              y: 2.61,
            },
          ],
        },
      ],
    });
  },
};
</script>

<style></style>
