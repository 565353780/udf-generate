#include "mesh_udf.h"
#include <igl/point_mesh_squared_distance.h>

std::vector<double> point_mesh_udf(const Eigen::MatrixXd &points,
                                   const Eigen::MatrixXd &verts,
                                   const Eigen::MatrixXi &faces) {
  Eigen::VectorXd sqr_d;
  Eigen::VectorXi I;
  Eigen::MatrixXd C;

  igl::point_mesh_squared_distance(points, verts, faces, sqr_d, I, C);

  Eigen::VectorXd d = sqr_d.array().sqrt();
  std::vector<double> result(d.data(), d.data() + d.size());
  return result;
}
