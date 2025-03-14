const LaunchDarkly = require("launchdarkly-node-server-sdk");

const client = LaunchDarkly.init("your-sdk-key");

client.on("ready", async () => {
  const enabled = await client.variation("new-feature", { key: "user123" }, false);
  console.log(`Feature flag enabled: ${enabled}`);
});
