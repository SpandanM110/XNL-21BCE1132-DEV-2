const { ApolloServer, gql } = require("apollo-server");

const typeDefs = gql`
  type User {
    id: ID!
    name: String!
  }
  type Query {
    getUser(id: ID!): User
  }
`;

const resolvers = {
  Query: {
    getUser: (_, { id }) => ({ id, name: "John Doe" }),
  },
};

const server = new ApolloServer({ typeDefs, resolvers });

server.listen(4000).then(({ url }) => {
  console.log(`🚀 GraphQL Server ready at ${url}`);
});
