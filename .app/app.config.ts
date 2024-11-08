/**
 * This file is used to configure the app
 *
 * If you have the "Cannot find name 'defineAppConfig'.ts(2304)" error
 * update the root tsconfig.json file to include the following:
 *
 *  "extends": "./.app/.nuxt/tsconfig.json"
 *
 */

export default defineAppConfig({
  tairo: {
    title: 'Tairo Quick Starter',
    sidebar: {
      circularMenu: {
        enabled: false,
        tools: [],
      },
      toolbar: {
        enabled: true,
        showTitle: true,
        showNavBurger: false,
        tools: [
          {
            // Use a global component
            component: 'DemoThemeToggle',
            // Define the component props, if any
            props: {
              disableTransitions: true,
            },
          },
        ],
      },
      navigation: {
        items: [
          {
            title: 'Dashboards',
            icon: { name: 'ph:sidebar-duotone', class: 'w-5 h-5' },
            activePath: '/dashboards',
            subsidebar: { component: 'DemoSubsidebarDashboards' },
            to: '/dashboards/messaging',
            // OR Custom action to trigger 
            // when clicking on the item
            click: () => {
              alert('clicked on layouts')
            },
          },
        ]
      }
    },
  },
})
