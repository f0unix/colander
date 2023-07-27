let COMPONENT_TRACK_IDS = {};

async function async_load_component(destJContainer, component_name) {
    let domResponse = await fetch(`/vues/${component_name}.vue`);
    let dom = await domResponse.text();
    destJContainer.append(dom);
    let jsResponse = await fetch( `/vues/${component_name}.vue?part=js`);
    let js = await jsResponse.text();
    let vueInstance = eval(js);
    vueInstance.$mount(destJContainer.find('.vue-container').get(0));
    //let newJContainer = $(vueInstance.$el);
    destJContainer.data('vue', vueInstance);
    destJContainer.trigger('vue-ready', [destJContainer, vueInstance]);
    return `Vue component ready: ${component_name}`;
}
export const vueComponent = (component_name) => {
    COMPONENT_TRACK_IDS[component_name] = COMPONENT_TRACK_IDS[component_name] || 0;
    COMPONENT_TRACK_IDS[component_name]++;
    let jContainer = $(`<div id='${component_name}-${COMPONENT_TRACK_IDS[component_name]}' class="vue-component"/>`);
    async_load_component(jContainer, component_name)
        .then(console.log)
        .catch(console.error);
    return jContainer;
};
