
import { useService } from "@web/core/utils/hooks";
import { useEffect } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { JournalDashboardGraphField } from "@web/views/fields/journal_dashboard_graph/journal_dashboard_graph_field";

export class EmiproDashboardGraph extends JournalDashboardGraphField {
    static template = "shopify_lib.graph";
    setup() {
        super.setup();
        console.log("data canvasRef", this.canvasRef);
        console.log("data", this);
        this.data = this.props.record.data
        this.match_key = Object.keys(this.data).find(key => key.includes('_order_data'));
        console.log("match",this.data['shopify_order_data']);
        
        console.log("match_key", this.match_key);
        this.graph_data = this.match_key ? JSON.parse(this.data[this.match_key]) : {};
        console.log("graph data", this.graph_data);
        
        this.context = this.props.record.context;
        this.actionService = useService("action");

        this.orm = useService("orm");

        useEffect(() => {
            this.renderChart();
            console.log("calleduseEffect");
            
            return () => {
                if (this.chart) {
                    this.chart.destroy();
                }
            };
        },
        () => [this.context.sort]
    );
    }

    getLineChartConfig() {
        console.log("called getLineChartConfig", this.graph_data);
        
        if (this.graph_data && this.graph_data.values) {
            const labels = this.graph_data.values.map(pt => pt.x);
            const borderColor = '#0068ff';
            const backgroundColor = '#ebebeb';
            return {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        data: this.graph_data.values,
                        fill: 'start',
                        label: this.graph_data.key,
                        backgroundColor: backgroundColor,
                        borderColor: borderColor,
                        borderWidth: 2,
                        pointStyle: 'line',
                    }]
                },
                options: {
                    plugins: {
                        legend: { display: false },
                    },
                    scales: {
                        x: { position: 'bottom' },
                        y: { position: 'left', beginAtZero: true },
                    },
                    maintainAspectRatio: false,
                    elements: { line: { tension: 0.5 } },
                    interaction: { intersect: false, mode: 'nearest' },
                },
            };
        }
    }

    _sortOrders(e) {
        console.log("sort vale", e.target.value);
          this.context.sort = e.currentTarget.value;
          console.log("res id ", this.props.record.evalContext.id);
          
          this.orm.silent.call("shopify.instance.ept", "read", [[this.props.record.evalContext.id]], {
            context: {
                'sort': e.currentTarget.value
            }
        }
        )
          .then((result) => {
            console.log("sort vale result", result.length);
            if (result.length) {
                this.graph_data = JSON.parse(result[0][this.match_key]);
                this.renderChart();
            }
          })
      }

    _performOpration() {
        this.orm.silent.call("shopify.instance.ept", "perform_operation", [this.props.record.evalContext.id])
          .then((result) => {
            return this.actionService.doAction(result);
          })
    }

    _getReport() {
        this.orm.silent.call("shopify.instance.ept", "open_report", [this.props.record.evalContext.id])
          .then((result) => {
            return this.actionService.doAction(result);
          })
    }

    _getLog() {
        this.orm.silent.call("shopify.instance.ept", "open_logs", [this.props.record.evalContext.id])
          .then((result) => {
            return this.actionService.doAction(result);
          })
    }

    _getProducts() {
        return this.actionService.doAction(this.graph_data.product_date.product_action);
    }

    _getCustomers() {
        console.log("customer data,",this.graph_data.customer_data.customer_action);
        
        return this.actionService.doAction(this.graph_data.customer_data.customer_action);
    }

    _getOrders() {
        return this.actionService.doAction(this.graph_data.order_data.order_action);
    }

    _getShippedOrders() {
        return this.actionService.doAction(this.graph_data.order_shipped.order_action);
    }

    _getRefundOrders() {
        return this.actionService.doAction(this.graph_data.refund_data.refund_action);
    }
}

export const emiproDashboardGraph = {
    component: EmiproDashboardGraph,
    supportedTypes: ["text"],
    extractProps: ({ attrs }) => ({
        graphType: attrs.graph_type,
    }),
};

registry.category("fields").add("dashboard_graph_ec", emiproDashboardGraph);

